Name:           python-colored
Version:        2.2.2
Release:        1%{?dist}
Summary:        Library for color and formatting in terminal

License:        MIT
URL:            https://gitlab.com/dslackw/colored
Source:         https://gitlab.com/dslackw/colored/-/archive/%{version}/colored-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Very simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups.}

%description %_description

%package -n python3-colored
Summary:        %{summary}

%description -n python3-colored %_description


%prep
%autosetup -p1 -n colored-%{version}
# remove shebangs
sed -i '/#!\/usr\/bin\/env python/d' colored/*.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colored


%check
# tests from upstream appear to be incomplete and/or things that must be run manually.
%pyproject_check_import colored


%files -n python3-colored -f %{pyproject_files}
%doc README.* CHANGES.md


%changelog
* Mon Jun 26 2023 Jonathan Wright <jonathan@almalinux.org> - 2.2.2-1
- Update to 2.2.2 rhbz#2215743

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.4-2
- Rebuilt for Python 3.12

* Thu Jan 12 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.4-1
- Initial package build
