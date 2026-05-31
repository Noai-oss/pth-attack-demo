from pathlib import Path

from setuptools import setup
from setuptools.command.sdist import sdist as _sdist
# from setuptools.command.install import install as _install
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.editable_wheel import editable_wheel as _editable_wheel

PTH_NAME = "attack.pth"


class build_py(_build_py):
    # build_py used by projects with pymodule
    def copy_redirector_file(self, source, destination="."):
        destination = Path(self.build_lib) / destination / source
        self.copy_file(str(source), str(destination), preserve_mode=False)

    def run(self):
        super().run()
        
        self.copy_redirector_file(PTH_NAME)
    
    def get_output_mapping(self) -> dict[str, str]:
        mapping = super().get_output_mapping()
        mapping[str(Path(self.build_lib) / PTH_NAME)] = PTH_NAME
        return mapping
    
    def get_source_files(self):
        src = super().get_source_files()
        src.append(PTH_NAME)
        return src


# class install(_install):
#     def run(self) -> None:
#         super().run()
#         target = Path(self.install_libbase) / PTH_NAME
#         self.mkpath(str(target.parent))
#         self.copy_file(PTH_NAME, str(target))

#     def get_outputs(self):
#         return super().get_outputs() + [
#             str(Path(self.install_libbase) / PTH_NAME)
#         ]

class sdist(_sdist):
    def make_release_tree(self, base_dir, files) -> None:
        super().make_release_tree(base_dir, files)

        target = Path(base_dir) / PTH_NAME
        self.copy_file(PTH_NAME, str(target))

class editable_wheel(_editable_wheel):
    def _select_strategy(self, name, tag, build_lib):
        base_strategy = super()._select_strategy(name, tag, build_lib)

        class Strategy:
            def __enter__(self):
                base_strategy.__enter__()
                return self
        
            def __exit__(self, exc_type, exc_value, traceback):
                return base_strategy.__exit__(exc_type, exc_value, traceback)
            
            def __call__(self, wheel, files, mapping):
                base_strategy(wheel, files, mapping)

                wheel.write(
                    PTH_NAME,
                    PTH_NAME,
                )
        return Strategy()


setup(
    cmdclass={
        "build_py": build_py,
        # "install": install,
        "sdist": sdist,
        "editable_wheel": editable_wheel,
    },
)
