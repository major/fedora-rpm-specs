Name:           atari++
Version:        1.85
Release:        8%{?dist}
Summary:        Unix based emulator of the Atari 8-bit computers

# Automatically converted from old format: TPL - review is highly recommended.
License:        TPL-1.0
URL:            http://www.xl-project.com/
Source0:        http://www.xl-project.com/download/%{name}_%{version}.tar.gz
Source1:        http://www.xl-project.com/download/os++doc.pdf
Source2:        http://www.xl-project.com/download/basic++doc.pdf
Source3:        http://www.xl-project.com/download/system.atr
Source4:        %{name}.desktop
# borrowed from atari800 project
Source5:        atari2.svg
# be verbose during compile
Patch1:         %{name}-verbose.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  zlib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make


%description
The Atari++ Emulator is a Unix based emulator of the Atari 8-bit
computers, namely the Atari 400 and 800, the Atari 400XL, 800XL and 130XE,
and the Atari 5200 game console. The emulator is auto-configurable and
will compile on a variety of systems (Linux, Solaris, Irix).
Atari++ 1.30 and up contain a built-in ROM emulation that tries to mimic
the AtariXL operating system closely.


%prep
%autosetup -p1 -n %{name}

# fix encoding
f=README.History
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

# fix permissions for sources
chmod a-x *.cpp *.hpp

# additional docs
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%configure
%{make_build} OPTIMIZER="%{build_cflags} -DDEBUG_LEVEL=0 -DCHECK_LEVEL=0" LDFLAGS="%{build_ldflags} -lSDL"


%install
make install DESTDIR=%{buildroot}

# remove installed docs
rm -rf %{buildroot}%{_docdir}/%{name}

# install system disk into %%_datadir
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}

# install icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps

# desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications           \
        %{SOURCE4}


%files
%license COPYRIGHT README.licence
%doc CREDITS README.LEGAL README.History manual
%doc os++doc.pdf basic++doc.pdf
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/atari2.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.85-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Dan Horák <dan[at]danny.cz> - 1.85-1
- updated to version 1.85 (rhbz#2156202)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Dan Horák <dan[at]danny.cz> - 1.84-1
- updated to version 1.84
- modernized spec

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Dan Horák <dan[at]danny.cz> - 1.83-1
- updated to version 1.83

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Dan Horák <dan[at]danny.cz> - 1.81-1
- updated to version 1.81 (#1405251)
- add desktop integration (#1353851)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Dan Horák <dan[at]danny.cz> - 1.80-1
- updated to version 1.80

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.73-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Dan Horák <dan[at]danny.cz> - 1.73-4
- switch to polling for Alsa sound (#1201805)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Dan Horák <dan[at]danny.cz> - 1.73-1
- updated to version 1.73

* Tue Dec 03 2013 Dan Horák <dan[at]danny.cz> 1.72-3
- fix build with -Werror=format-security (#1036993)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Dan Horák <dan[at]danny.cz> 1.72-1
- updated to version 1.72

* Thu Jan 31 2013 Dan Horák <dan[at]danny.cz> 1.71-1
- updated to version 1.71

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.60-2
- Rebuild for new libpng

* Fri May 13 2011 Dan Horák <dan[at]danny.cz> 1.60-1
- updated to version 1.60

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 30 2009 Dan Horák <dan[at]danny.cz> 1.58-1.1
- rebuilt with updated source archive

* Mon Nov 30 2009 Dan Horák <dan[at]danny.cz> 1.58-1
- updated to version 1.58
- used better patch for the making the build output verbose

* Tue Aug 25 2009 Dan Horák <dan[at]danny.cz> 1.57-1
- update to version 1.57

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Dan Horák <dan[at]danny.cz> 1.56-2
- add patch for sparc

* Mon May 18 2009 Dan Horák <dan[at]danny.cz> 1.56-1
- update to version 1.56

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Dan Horák <dan[at]danny.cz> 1.55-2
- disable the verbose patch

* Wed Nov 19 2008 Dan Horák <dan[at]danny.cz> 1.55-1
- initial Fedora version
