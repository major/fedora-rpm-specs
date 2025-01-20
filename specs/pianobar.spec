%global baseurl https://6xq.net
%global common_description %{expand:
pianobar is a free/open-source, console-based client for the personalized
online radio Pandora.}

Name:           pianobar
Version:        2022.04.01
Release:        12%{?dist}
Summary:        Console-based client for Pandora

License:        MIT
URL:            %{baseurl}/%{name}
Source:         %{url}/%{name}-%{version}.tar.bz2
Source:         %{url}/%{name}-%{version}.tar.bz2.sha256
Source:         %{url}/%{name}-%{version}.tar.bz2.asc
Source:         %{baseurl}/08D8092A.gpg
# Add compatibility with FFMPEG 7.0
Patch:          https://github.com/PromyLOPh/pianobar/commit/8bf4c1bbaa6a533f34d74f83d72eecc0beb61d4f.patch

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  gnutls-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmad-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  json-c-devel

BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavfilter)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    %{common_description}

Features
* play and manage (create, add more music, delete, rename, ...) stations
* rate songs and explain why they have been selected
* upcoming songs/song history
* customize keybindings and text output
* remote control and eventcmd interface (send tracks to last.fm, for example)
* proxy support for listeners outside the USA

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains development headers and libraries for %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}

This package contains shared libraries for %{name}.

%prep
%autosetup -p1

# Verify source tarball
(cd "%{_sourcedir}" && sha256sum --check "%{SOURCE1}")
%{gpgverify} --keyring="%{SOURCE3}" --signature="%{SOURCE2}" --data="%{SOURCE0}"

# Preserve timestamps on install
sed -i 's/install /install -p /g' Makefile

%build
%make_build DYNLINK=1 V=1

%install
%make_install DYNLINK=1 PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# Fix shared library permissions
chmod +x %{buildroot}%{_libdir}/libpiano.so.0.0.0

# We don't want the static library
rm %{buildroot}%{_libdir}/libpiano.a

%files
%doc ChangeLog README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/piano.h
%{_libdir}/libpiano.so

%files libs
%license COPYING
%{_libdir}/libpiano.so.0{,.*}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022.04.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Robert-André Mauchin <zebob.m@gmail.com> - 2022.04.01-11
- Add patch for FFMPEG 7 compatibility

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 2022.04.01-10
- Rebuild for ffmpeg 7

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.04.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.04.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.04.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2022.04.01-6
- Add library dependency to the main package
- Fix globbing for shared libraries

* Wed Aug 23 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2022.04.01-5
- Adjust BuildRequires for ffmpeg
- Perform checksum and signature checking for source tarball
- Preserve timestamps on install
- Package shared library and development headers

* Tue Aug 22 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2022.04.01-4
- Rework specfile to follow the Fedora packaging guidelines
- Drop unused BuildRequires on faad2-devel
- Drop unnecessary Requires on ffmpeg-libs

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 2022.04.01-3
- Rebuild for new ffmpeg

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2022.04.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sun Apr 17 2022 Leigh Scott <leigh123linux@gmail.com> - 2022.04.01-1
- Update to 2022.04.01

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2020.11.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 2020.11.28-2
- Rebuilt for new ffmpeg snapshot

* Sun Nov 07 2021 Richard Shaw <hobbes1069@gmail.com> - 2020.11.28-1
- Update to 2020.11.28.

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2020.04.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2020.04.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 2020.04.05-4
- Rebuilt for new ffmpeg snapshot

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2020.04.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Leigh Scott <leigh123linux@gmail.com> - 2020.04.05-2
- Rebuilt for libjson

* Mon Apr 06 2020 Richard Shaw <hobbes1069@gmail.com> - 2020.04.05-1
- Update to 2020.04.05.

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2019.02.14-4
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2019.02.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 2019.02.14-2
- Rebuild for new ffmpeg version

* Mon Jul 01 2019 Richard Shaw <hobbes1069@gmail.com> - 2019.02.14-1
- Update to 2019.02.14.

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2017.08.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2017.08.30-7
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2017.08.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 2017.08.30-5
- Rebuilt for libjson

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2017.08.30-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2017.08.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2017.08.30-2
- Rebuilt for ffmpeg-3.5 git

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 2017.08.30-1
- Update to latest upstream release.
- Fix debuginfo issue (actually call configure)

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.06.02-4
- Disable debuginfo

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2016.06.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-2
- Use configure so linker flags are utilized.

* Thu Jul 21 2016 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-1
- Update to latest upstream release.

* Fri Feb  1 2013 Richard Shaw <hobbes1069@gmail.com> - 2013.09.15-1
- Initial packaging.
