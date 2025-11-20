Name:           python-sphinx-lint
Version:        1.0.2
Release:        %autorelease
Summary:        Check stylistic and formal issues in .rst and .py files in the documentation
License:        PSF-2.0
URL:            https://github.com/sphinx-contrib/sphinx-lint
Source:         %{url}/archive/v%{version}/sphinx-lint-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Sphinx Lint should:

- be reasonably fast so it's comfortable to use as a linter in your editor.
- be usable on a single file.
- not give any false positives (probably a utopia, but let's try).
- not spend too much effort finding errors that sphinx-build already finds (or
can easily find).
- focus on finding errors that are not visible to sphinx-build.
}

%description %_description

%package -n     python3-sphinx-lint
Summary:        %{summary}

%description -n python3-sphinx-lint %_description

%pyproject_extras_subpkg -n python3-sphinx-lint tests

%prep
%autosetup -p1 -n sphinx-lint-%{version}

# adopted from python-sphinx-argparse-cli package
sed -i '/name = "sphinx-lint"/a version = "%{version}"' \
    pyproject.toml
sed -i '/version.source = "vcs"/d' pyproject.toml
sed -i '/"version",/{n;d;}' pyproject.toml
sed -i '/  "version",/d' pyproject.toml
sed -i '/^dynamic = \[/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxlint

%check
%pyproject_check_import
%pytest

%files -n python3-sphinx-lint -f %{pyproject_files}
%{_bindir}/sphinx-lint

%changelog
%autochangelog
