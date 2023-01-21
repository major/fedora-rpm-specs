Name:           libimagequant
Version:        2.17.0
Release:        4%{?dist}
Summary:        Palette quantization library

License:        GPLv3+ and MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Small, portable C library for high-quality conversion of RGBA images to 8-bit
indexed-color (palette) images.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%configure --with-openmp
%make_build


%install
%make_install

# Don't ship static library
rm -f %{buildroot}%{_libdir}/%{name}.a


%ldconfig_scriptlets


%files
%license COPYRIGHT
%doc README.md CHANGELOG
%{_libdir}/%{name}.so.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/imagequant.pc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Sandro Mani <manisandro@gmail.com> - 2.17.0-1
- Update to 2.17.0

* Tue Sep 21 2021 Sandro Mani <manisandro@gmail.com> - 2.16.0-1
- Update to 2.16.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Sandro Mani <manisandro@gmail.com> - 2.15.1-1
- Update to 2.15.1

* Wed May 12 2021 Sandro Mani <manisandro@gmail.com> - 2.15.0-1
- Update to 2.15.0

* Wed Mar 03 2021 Sandro Mani <manisandro@gmail.com> - 2.14.1-1
- Update to 2.14.1

* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Sandro Mani <manisandro@gmail.com> - 2.13.1-1
- Update to 2.13.1

* Mon Oct 19 2020 Sandro Mani <manisandro@gmail.com> - 2.13.0-1
- Update to 2.13.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Sandro Mani <manisandro@gmail.com> - 2.12.6-1
- Update to 2.12.6

* Mon Jul 29 2019 Sandro Mani <manisandro@gmail.com> - 2.12.5-1
- Update to 2.12.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Sandro Mani <manisandro@gmail.com> - 2.12.3-1
- Update to 2.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Sandro Mani <manisandro@gmail.com> - 2.12.2-1
- Update to 2.12.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 2.12.1-1
- Update to 2.12.1

* Mon Mar 12 2018 Sandro Mani <manisandro@gmail.com> - 2.11.10-1
- Update to 2.11.10

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.11.7-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Sandro Mani <manisandro@gmail.com> - 2.11.7-1
- Update to 2.11.7

* Thu Jan 18 2018 Sandro Mani <manisandro@gmail.com> - 2.11.6-1
- Update to 2.11.6

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 2.11.4-1
- Update to 2.11.4

* Sat Nov 11 2017 Sandro Mani <manisandro@gmail.com> - 2.11.3-1
- Update to 2.11.3

* Sun Nov 05 2017 Sandro Mani <manisandro@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Tue Aug 08 2017 Sandro Mani <manisandro@gmail.com> - 2.10.2-1
- Update to 2.10.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Mon Jul 03 2017 Sandro Mani <manisandro@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Thu Apr 06 2017 Sandro Mani <manisandro@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Sat Mar 04 2017 Sandro Mani <manisandro@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 2.8.2-2
- Use %%name and %%url to reduce text

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 2.8.2-1
- Initial package
