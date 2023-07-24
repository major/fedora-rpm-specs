Name:		tucnak
Version:	4.44
Release:	3%{?dist}
Summary:	HF/VHF contest logging program
License:	GPLv2
URL:		http://tucnak.nagano.cz/
Source0:	http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Source1:	cz.nagano.Tucnak.metainfo.xml
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libzia-devel = %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	fftw-devel
BuildRequires:	hamlib-devel
BuildRequires:	rtl-sdr-devel
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel
BuildRequires:	binutils-devel
BuildRequires:	gnutls-devel
# For fixing files encoding
BuildRequires:	recode
Requires:	hicolor-icon-theme
Provides:	tucnak2 = %{version}-%{release}
Obsoletes:	tucnak2 < 2.31-21
# This is to rename soundwrapper from the generic name to the
# tucnak-soundwrapper, it can avoid name conflicts with other
# soundwrappers possibly shipped by other packages in the future.
Patch0:		tucnak-4.18-soundwrapper.patch

%description
Tucnak is HF/VHF/UHF/SHF log for hamradio contests. It supports multi
bands, free input, networking, voice and CW keyer, WWL database and
much more.

%prep
%autosetup -p1

# fix encoding to UTF-8
recode ISO-8859-2..UTF-8 AUTHORS ChangeLog

%build
autoreconf -fi
%configure

# temporal LIBS workaround for rhbz#2174841
%if 0%{fedora} > 38
  LIBS="-lsframe"
%else
  LIBS=""
%endif
%make_build LIBS="$LIBS"

%install
%make_install

# Install icon
install -D -p -m644 data/tucnak64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install AppStream metainfo file
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml

# rename soundwrapper to tucnak-soundwrapper
mv %{buildroot}%{_bindir}/soundwrapper %{buildroot}%{_bindir}/tucnak-soundwrapper 

# drop docs installed to wrong place
rm -f %{buildroot}%{_datadir}/tucnak/doc/*
rmdir %{buildroot}%{_datadir}/tucnak/doc

# drop unneeded files/dirs
rm -f %{buildroot}%{_prefix}/lib/tucnak/tucnak.d
rmdir %{buildroot}%{_prefix}/lib/tucnak

%files
%license COPYING
%doc AUTHORS ChangeLog TODO
%doc doc/NAVOD.pdf doc/NAVOD.sxw
%doc data/*.html data/*.png
%{_bindir}/tucnak
%{_bindir}/tucnak-soundwrapper
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/*
%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml
%{_datadir}/%{name}

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Daniel Rusek <mail@asciiwolf.com> - 4.44-2
- Added AppStream metadata, small fixes
  Resolves: rhbz#1476482

* Mon Jun  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.44-1
- New version
  Resolves: rhbz#2212154

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.43-1
- New version
  Resolves: rhbz#2186987

* Mon Mar 13 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.42-1
- New version
  Resolves: rhbz#2177170

* Tue Mar  7 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.41-1
- New version
  Resolves: rhbz#2175029

* Sat Feb 04 2023 Florian Weimer <fweimer@redhat.com> - 4.40-3
- Port configure script to C99 (#2167084)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.40-1
- New version
  Resolves: rhbz#2159136

* Tue Dec 13 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.39-1
- New version
  Resolves: rhbz#2152850

* Thu Dec  1 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.38-1
- New version
  Resolves: rhbz#2148552

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 4.37-2
- Rebuild for hamlib 4.5.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.37-1
- New version
  Resolves: rhbz#2128090

* Thu Aug  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-3
- Fixed FTBFS
  Resolves: rhbz#2113748

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May  3 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.36-1
- New version
  Resolves: rhbz#2080501

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.35-1
- New version
  Resolves: rhbz#2074482

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.34-4
- Rebuilt for libzia with SDL2

* Sun Jan  2 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.34-3
- Rebuilt for new libzia

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.34-2
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.34-1
- New version
  Resolves: rhbz#2033563

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.32-3
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 4.32-2
- Rebuild for hamlib 4.3.1.

* Tue Oct  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.32-1
- New version
  Resolves: rhbz#2009257

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.30-1
- New version
  Resolves: rhbz#1977455

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 4.29-2
- Rebuild for hamlib 4.2.

* Mon May 24 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.29-1
- New version
  Resolves: rhbz#1963426

* Wed Apr 21 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.28-1
- New version
  Resolves: rhbz#1952087

* Wed Apr 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.27-1
- New version
  Resolves: rhbz#1949451

* Fri Apr  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.26-1
- New version

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 4.24-3
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.24-1
- New version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 4.20-3
- Rebuild for hamlib 4.

* Thu Feb  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-2
- Variuos fixes according to the review

* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-1
- New version

* Tue Jan 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.19-1
- New version
- Fixed according to the review

* Fri Jan  3 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-1
- Initial version
