%global sname pyvat
%global owner iconfinder

Name:       python-%{sname}
Version:    1.3.17
Release:    6%{?dist}
Summary:    VAT validation and calculation for Python
License:    ASL 2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}
BuildArch:  noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
Requires:       python3

%description
With EU VAT handling rules becoming ever more ridiculous and complicated,
businesses within the EU are faced with the complexity of having to
validate VAT numbers. pyvat was built for
Iconfinder's marketplace to handle just this problem.

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
With EU VAT handling rules becoming ever more ridiculous and complicated,
businesses within the EU are faced with the complexity of having to
validate VAT numbers. pyvat was built for
Iconfinder's marketplace to handle just this problem.

%prep
%autosetup -p1 -n %{sname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

# check
# These tests require unittest2 to run as the project is compatible with Python 2 versions
# unittest2 was intentially removed from Fedora repositories see https://bugzilla.redhat.com/show_bug.cgi?id=1794222

%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.17-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Italo Garcia <italo.garcia@aiven.io> - 1.3.17-1
- Update to 1.3.17

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.16-2
- Drop support for i686

* Mon Sep 19 2022 Roman Inflianskas <rominf@aiven.io> - 1.3.16-1
- Update to 1.3.16

* Tue Jul 19 2022 Italo Garcia <italo.garcia@aiven.io> - 1.3.15-1
- Initial package
