Name:		python-hsluv
Version:	5.0.4
Release:	4%{?dist}
Summary:	A Python implementation of HSLuv (revision 4)
License:	MIT
URL:		https://www.hsluv.org/
Source0:	%{pypi_source hsluv}

BuildArch:	noarch
BuildRequires:	python3-devel

# Tests
BuildRequires:	python3dist(pytest)

%global _description %{expand:
A Python implementation of HSLuv (revision 4).}


%description %_description

%package -n python3-hsluv
Summary: %{summary}

%description -n python3-hsluv %_description


%prep
%autosetup -p1 -n hsluv-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l hsluv


%check
%pytest
%pyproject_check_import


%files -n python3-hsluv -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 José Matos <jamatos@fedoraproject.org> - 5.0.4-2
- Minor cleanup: source location and removal of extraneous dependency

* Tue Feb 06 2024 José Matos <jamatos@fedoraproject.org> - 5.0.4-1
- First version
