%global forgeurl https://github.com/pchev/libpasastro/

Version:        1.4.1
%forgemeta

Name:           libpasastro
Release:        4%{?dist}
Summary:        Pascal interface for standard astronomy libraries

License:        GPLv2+
URL:            %{forgeurl}
Source0:        %{forgesource}

# Patch to fix stripping of library files
# Since this is Fedora specific we don't ask upstream to include
Patch1:         libpasastro-1.3-nostrip.patch

# Add LDFLAGS to compiler
Patch2:         libpasastro-1.4-ldflags.patch

BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       bundled(wcstools) = 3.9.5

%description
Libpasastro provides shared libraries to interface Pascal program 
with standard astronomy libraries.
libpasgetdss.so : Interface with GetDSS to work with DSS images.
libpasplan404.so : Interface with Plan404 to compute planets position.
libpaswcs.so : Interface with libwcs to work with FITS WCS.
The library libpasspice.so is not distributed in the Fedora package
due to unclear license.


%prep
%forgeautosetup -p1

# do not install docs, use %%doc macro
sed -i '/\$destdir\/share/d' ./install.sh

# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh


%build
%make_build arch_flags="%{optflags}" FED_LDFLAGS="%{build_ldflags}"


%install
make install PREFIX=%{buildroot}%{_prefix}


%files
%doc changelog copyright README.md
%{_libdir}/libpas*.so.1
%{_libdir}/libpas*.so.1.1


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 Mattia Verga <mattia.verga@protonmail.com> - 1.4.1-1
- Update to 1.4.1
- spice sources have been removed upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.4.0-1
- Update to 1.4.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.3.0-1
- Update to 1.3.0
- libpasraw is now in a separate package on its own
- Use fedora ldflags in build macro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9.20191024git4360b2a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Mattia Verga <mattia.verga@protonmail.com> - 1.1-8.20191024git4360b2a
- Update to git 4360b2a
- Added libpasraw.so
- Need LibRaw-devel as Build Require

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7.20171110svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.20171110svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.20171110svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Mattia Verga <mattia.verga@yandex.com> - 1.1-4.20171110svn
- Remove ldconfig scriptlets

* Mon Feb 19 2018 Mattia Verga <mattia.verga@email.it> - 1.1-3.20171110svn
- Add gcc-c++ as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2.20171110svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Mattia Verga <mattia.verga@email.it> - 1.1-1.20171110svn
- Update to 1.1 rev 20

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20160111svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20160111svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.20160111svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160111svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-6.20160111svn
- Update to svn rev 9

* Fri Jan 1 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-5.20151222svn
- Remove fpc and lazarus BR and remove ExcludeArch
- Update to svn rev 6
- Use optflags for debugging generation and remove hardcoded patch

* Sun Dec 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-4.20151219svn
- Properly set ExcludeArch

* Sun Dec 20 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-3.20151219svn
- Better symlinks creation

* Sat Dec 19 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-2.20151219svn
- Use svn updated sources
- Create symlinks to soname

* Fri Dec 18 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.0-1
- Initial release
