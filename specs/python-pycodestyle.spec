Name:           python-pycodestyle
# WARNING: When updating pycodestyle, check not to break flake8!
Version:        2.12.1
Release:        %autorelease
Summary:        Python style guide checker
License:        MIT
URL:            https://pypi.python.org/pypi/pycodestyle
# pypi source missing docs - https://github.com/PyCQA/pycodestyle/issues/1231
Source0:        https://github.com/PyCQA/pycodestyle/archive/%{version}/pycodestyle-%{version}.tar.gz

BuildArch:      noarch

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.


%package -n python%{python3_pkgversion}-pycodestyle
Summary:    Python style guide checker
Conflicts:      python-pycodestyle < %{version}-%{release}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  make

%description -n python%{python3_pkgversion}-pycodestyle
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.

This is a version for Python %{python3_pkgversion}.


%prep
%autosetup -n pycodestyle-%{version} -p1

# Remove #! from pycodestyle.py
sed --in-place "s:#!\s*/usr.*::" pycodestyle.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

make -C docs man SPHINXBUILD=sphinx-build-%{python3_version}


%install
%pyproject_install
%pyproject_save_files -l pycodestyle
mv %{buildroot}%{_bindir}/pycodestyle %{buildroot}%{_bindir}/pycodestyle-%{python3_version}
ln -s ./pycodestyle-%{python3_version} %{buildroot}%{_bindir}/pycodestyle-3
ln -s ./pycodestyle-3 %{buildroot}%{_bindir}/pycodestyle


install -D docs/_build/man/pycodestyle.1 %{buildroot}%{_mandir}/man1/pycodestyle.1


%check
%pyproject_check_import
%pytest -v


%files -n python%{python3_pkgversion}-pycodestyle -f %{pyproject_files}
%doc README.rst CHANGES.txt
%{_mandir}/man1/pycodestyle.1.gz
%{_bindir}/pycodestyle
%{_bindir}/pycodestyle-3
%{_bindir}/pycodestyle-%{python3_version}

%changelog
%autochangelog
