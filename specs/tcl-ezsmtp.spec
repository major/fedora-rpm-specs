%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}
%global extname ezsmtp

Name:           tcl-%{extname}
Version:        1.0.0
Release:        9%{?dist}
Summary:        Easy SMTP for TCL

License:        TCL and MIT
# the original website for ezsmtp is long gone
URL:            https://web.archive.org/web/20020602055052/http://www.millibits.com/djh/tcl
# archive.org will serve tar.gz as tar, so rename accordingly
Source0:        %{url}/%{extname}%{version}.tar.gz#/%{extname}%{version}.tar

BuildRequires:  tcl

Requires:       tcl(abi) = 8.6
Provides:       %{extname} = %{version}-%{release}

BuildArch:      noarch

%description
Easy SMTP (ezsmtp) is a simple 100%-pure-Tcl cross-platform package for
sending text email, based on original work by Keith Vetter at UC Berkeley.

%prep
%setup -q -n %{extname}%{version}
mkdir -p examples
mv koi8-r-body.txt test_examples.txt postinst.tcl examples/

%build

%install
mkdir -p %{buildroot}%{tcl_sitelib}/ezsmtp
cp -P ezsmtp.tcl %{buildroot}%{tcl_sitelib}/ezsmtp

%files
%license license.txt
%doc README.txt ChangeLog ezsmtp.html
%doc examples
%{tcl_sitelib}/ezsmtp

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1
- Initial package
