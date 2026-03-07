%global extras mkdocs,trio,toml,yaml

Name:           python-cyclopts
Version:        4.7.0
Release:        %autorelease
Summary:        Intuitive, easy CLIs based on type hints

License:        Apache-2.0
URL:            https://github.com/BrianPugh/cyclopts
# We are using the github tarball due to the lack of tests being present in the
# pypi sources.
Source:         %{url}/archive/v%{version}/cyclopts-%{version}.tar.gz

# Sources needed for intersphinx to build the manpages properly.
# Pydantic:          MIT
Source1:        https://docs.pydantic.dev/latest/objects.inv#/objects-pydantic.inv
# Python:            Python-2.0.1
Source2:        https://docs.python.org/3/objects.inv#/objects-python.inv
# Rich:              MIT
Source3:        https://rich.readthedocs.io/en/stable/objects.inv#/objects-rich.inv
# Typing Extensions: PSF-2.0
Source4:        https://typing-extensions.readthedocs.io/en/latest/objects.inv#/objects-typing-extensions.inv
# Pytest:            MIT
Source5:        https://docs.pytest.org/en/latest/objects.inv#/objects-pytest.inv

# The modifications applied to this patch are meant to make `make man` works during the build steps.
# - Changes to this patch:
#     * Created a new stub-class `GitRepo` that provides an `working_dir`
#     property to bypass the behavior of GitPython, due to the lack of the
#     `.git` folder in the sources. The code is always checking for the root
#     directory in order to link the source files against it
#
#     * Patched `git_commit` to use `__version__` instead of the commit hash
#     since we are pulling the version from github.
#
#     * Removed the sphinx_rtd_dark_mode, as we care only about the builds for
#     man pages, not html/pdf or anything else.
#
#     * Removed the html_logo and html_favicon variables as we don't want the
#     assets folder to be present in the sources.
Patch:          patch-docs-conf-for-downstream-build.diff
# Change from `autoexception` to `autoclass` the exception classes that are
# inherinting from `Exception` directly instead of `CycloptsError`, due to
# sphinx not being able to call `autodoc` on it.
Patch1:         exclude-init-members-from-exception-class.diff

BuildArch:      noarch

BuildRequires:  python3-devel

# Docs dependencies
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-linkify-it-py

# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-syrupy
BuildRequires:  python3-pydantic
BuildRequires:  python3-pytest-mock

%global _description %{expand:
Cyclopts is a modern, easy-to-use command-line interface (CLI) framework that
aims to provide an intuitive & efficient developer experience.}

%description %_description

%package -n     python3-cyclopts
Summary:        %{summary}


%description -n python3-cyclopts %_description

%pyproject_extras_subpkg -n python3-cyclopts %{extras}


%prep
%autosetup -p1 -n cyclopts-%{version}

# Use local objects.inv for intersphinx
sed -E -i \
  -e 's|("https://docs\.pydantic\.dev/latest/",[[:space:]]*)None|\1"%{SOURCE1}"|' \
  -e 's|("https://docs\.python\.org/3",[[:space:]]*)None|\1"%{SOURCE2}"|' \
  -e 's|("https://rich\.readthedocs\.io/en/stable/",[[:space:]]*)None|\1"%{SOURCE3}"|' \
  -e 's|("https://typing-extensions\.readthedocs\.io/en/latest/",[[:space:]]*)None|\1"%{SOURCE4}"|' \
  -e 's|("https://docs\.pytest\.org/en/latest",[[:space:]]*)None|\1"%{SOURCE5}"|' \
  docs/source/conf.py

# We don't want any binary blobs to be present in the final sources.
rm -rf assets


%generate_buildrequires
# Let hatch-vcs/setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x %{extras}

%build
# Let hatch-vcs/setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

# Override the SPHINXBUILD variable in the Makefile so we use bare sphinx-build
# instead of calling `uv run sphinx-build`
export SPHINXBUILD=sphinx-build

pushd docs
make man
popd


%install
%pyproject_install
%pyproject_save_files -l cyclopts
install -D -m 644 docs/build/man/cyclopts.1 %{buildroot}%{_mandir}/man1/cyclopts.1


%check
%pyproject_check_import
%pytest --snapshot-update


%files -n python3-cyclopts -f %{pyproject_files}
%{_mandir}/man1/cyclopts.1*
%{_bindir}/cyclopts
%doc README.md


%changelog
%autochangelog
