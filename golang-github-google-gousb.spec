# Run tests in check section
# Requires a usb device
%bcond_with check

# https://github.com/google/gousb
%global goipath         github.com/google/gousb
Version:                1.1.1

%global common_description %{expand:
The gousb package is an attempt at wrapping the libusb library into a 
Go-like binding.}

%gometa

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:       pkgconfig(libusb)}

Name:           %{goname}
Release:        7%{?dist}
Summary:        Idiomatic Go bindings for libusb-1.0

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  pkgconfig(libusb)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gochecks
%endif

%gopkgfiles

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 21:40:00 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 23:37:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Jakub Jelen <jjelen@redhat.com> - 0-0.1.20200108git18f4c1d8
- First package for Fedora
