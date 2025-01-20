Name:           python-read-roi
Version:        1.6.0
Release:        12%{?dist}
Summary:        Read ROI files .zip or .roi generated with imagej

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/hadim/read-roi/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/pull/27.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(nose2)


%global _description %{expand:
Read ROI files .zip or .roi generated with ImageJ. 
Some format specifications are not implemented.
Most of "normal" ROI files should work.
Feel free to hack it and send me modifications.

}

%description %_description

%package -n python3-read-roi
Summary:        %{summary}

%description -n python3-read-roi %_description


%prep
%autosetup -n read-roi-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files read_roi


%check
PYTHONPATH='%{buildroot}%{python3_sitelib}' nose2




%files -n python3-read-roi -f %{pyproject_files}
%doc README.*
%license LICENSE*



%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.6.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 1.6.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.11

*Tue Nov 9 2021 Adeleye Opeyemi <adebola786 AT gmail DOT com> - 1.6.0-2
-updated spec file
*Thu Oct 28 2021 Adeleye Opeyemi <adebola786 AT gmail DOT com> - 1.6.0-1
-initial rpm
