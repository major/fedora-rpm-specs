%undefine __cmake_in_source_build
%global so_ver 1.0.3

Name:           zopfli
Version:        %{so_ver}
Release:        13%{?dist}
Summary:        Zlib compatible better compressor

License:        Apache-2.0
URL:            https://github.com/google/%{name}
Source0:        %{URL}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5%) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

%package        devel
Requires:       %{name} = %{version}-%{release}
Summary:        Development files for zopfli and zopflipng.

%description    devel
Devolopment files for zopfli and zopflipng.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%cmake -DZOPFLI_BUILD_SHARED=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc CONTRIBUTORS README README.zopflipng
%{_bindir}/%{name}
%{_bindir}/%{name}png

%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{so_ver}

%{_libdir}/lib%{name}png.so.1
%{_libdir}/lib%{name}png.so.%{so_ver}

%files          devel
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}png.so

%{_includedir}/%{name}.h
%{_includedir}/%{name}png_lib.h
%{_libdir}/cmake/Zopfli/*.cmake


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.3-1
- New upstream release 1.0.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.ef109ddgit-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.2.ef109ddgit-1
- Update to 1.0.2
- Create devel subpackage

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar  2 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-2
- Ship zopflipng

* Wed Feb 10 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-1
- Update to 1.0.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.0-1
- upstream release 1.0.0

* Sun Mar 03 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.20130303gitacc035
- initial spec
