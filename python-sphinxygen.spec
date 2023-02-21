Name:           python-sphinxygen
Version:        1.0.0
Release:        1%{?dist}
Summary:        A script to read Doxygen XML output and emit ReST for Sphinx

# All files under ISC, though some tests and
# unpackaged files are under 0BSD
License:        ISC
URL:            https://gitlab.com/drobilla/sphinxygen
# Source from Pypi does not include all test files
Source:        %{url}/-/archive/v%{version}/sphinxygen-v%{version}.tar.gz

BuildRequires:  sed
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  doxygen
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

BuildArch: noarch

%global _description %{expand:
Sphinxygen is a Python module/script that generates Sphinx markup to describe
a C API, from an XML description extracted by Doxygen.}

%description %_description

%package -n python3-sphinxygen
Summary:        %{summary}

%description -n python3-sphinxygen %_description


%prep
%autosetup -n sphinxygen-v%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxygen
# fix permissions
chmod 644 %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py
# remove shebang line
sed -i '/^#!\/usr\/bin/d' %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py

# install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 doc/sphinxygen.1 -t %{buildroot}%{_mandir}/man1/

%check
%pytest test


%files -n python3-sphinxygen -f %{pyproject_files}
%doc README.md NEWS
%{_bindir}/sphinxygen
%{_mandir}/man1/sphinxygen.1*
 
%changelog
* Thu Feb 09 2023 Benson Muite <benson_muite@emailplus.org> - 1.0.0-1
- Initial packaging
