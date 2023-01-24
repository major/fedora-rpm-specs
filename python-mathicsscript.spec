%global srcname mathicsscript
%global forgeurl https://github.com/Mathics3/mathicsscript

Name:           python-%{srcname}
Version:        5.0.0
Release:        %autorelease
Summary:        Terminal CLI to Mathics3

License:        GPL-3.0-only
URL:            https://mathics.org
# The PyPI version is missing requirements.txt breaking the dep generator
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
mathicsscript is a command-line interface to Mathics.}

%description %_description

%package -n     %{srcname}
Summary:        %{summary}
Provides:       python3-%{srcname} = %{version}-%{release}
Recommends:     mathicsscript[full] = %{version}-%{release}
Recommends:     asymptote

%description -n %{srcname} %_description

%pyproject_extras_subpkg -n %{srcname} full

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# Remove leftover test files we don't need
rm -r %{buildroot}%{python3_sitelib}/test

# Relocate fake_psviewer.py
mkdir -p %{buildroot}%{_libexecdir}/%{srcname}
mv %{buildroot}%{_bindir}/fake_psviewer.py %{buildroot}%{_libexecdir}/%{srcname}/
sed -i 's:fake_psviewer.py:%{_libexecdir}/%{srcname}/fake_psviewer.py:' \
  %{buildroot}%{python3_sitelib}/%{srcname}/config.asy

%check
%pytest

%files -n %{srcname} -f %{pyproject_files}
%license COPYING.txt
%doc README.rst NEWS.md
%{_bindir}/%{srcname}
%{_libexecdir}/%{srcname}/

%changelog
%autochangelog
