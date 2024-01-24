Name:           act
%global lname   AutomaticComponentToolkit
%global goipath github.com/Autodesk/%{lname}
Version:        1.6.0
Release:        12%{?dist}
Summary:        Automatic Component Toolkit
License:        BSD

%{?gometa}
%{?!gometa:BuildRequires: /usr/bin/go}

URL:            https://%{goipath}
Source0:        %{url}/archive/v%{version}/%{lname}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
The Automatic Component Toolkit (ACT) is a code generator that takes an
instance of an Interface Description Language file and generates a thin
C89-API, implementation stubs and language bindings of your desired software
component.

%prep
%autosetup -n %{lname}-%{version}

%build
%{?!gobuild:%global gobuild go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x}
%gobuild -o act Source/*.go

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -vp act %{buildroot}%{_bindir}/


%files
%doc README.md
%license LICENSE.md
%{_bindir}/act

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 1.6.0-7
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962 in
  golang}

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.0-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-1
- Initial package (#1819148)
