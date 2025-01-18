Name:		fox
# http://www.fox-toolkit.org/faq.html#VERSION
# For now, use stable one
Version:	1.6.58
Release:	2%{?dist}
Summary:	C++ based Toolkit for developing Graphical User Interfaces

# GPL-2.0-or-later:	adie
# GPL-2.0-or-later:	calculator
# GPL-2.0-or-later:	pathfinder
# GPL-2.0-or-later:	shutterbug
# GPL-2.0-or-later:	reswrap
#
# http://lists.fedoraproject.org/pipermail/legal/2010-October/001419.html
# Note that 1.7.x has switched to LGPLv3+ with exceptions
# LGPLv2+ with exceptions, for now remove "with exceptions"
# for SPDX identifier
#
# SPDX confirmed (once)
License:	LGPL-2.1-or-later
URL:		http://www.fox-toolkit.org/   
Source0:	http://fox-toolkit.org/ftp/%{name}-%{version}.tar.gz
# Change Adie.stx path
Patch0:	fox-1.6.49-adie-syspath.patch
Patch1:	fox-1.6.54-format-security.patch

BuildRequires:	gcc-c++

BuildRequires:	bzip2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libX11-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXft-devel
BuildRequires:	libXi-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXrender-devel
# 1.7.x can use libwebp
#BuildRequires:	libwebp-devel
BuildRequires:	zlib-devel
# Due to Patch1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make

%description
FOX is a C++ based Toolkit for developing Graphical User Interfaces 
easily and effectively. It offers a wide, and growing, collection of 
Controls, and provides state of the art facilities such as drag and drop,
selection, as well as OpenGL widgets for 3D graphical manipulation.
FOX also implements icons, images, and user-convenience features such as 
status line help, and tooltips.  Tooltips may even be used for 3D
objects.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	utils
Summary:	Utility applications based on %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}
# Note that 1.7.x has switched to GPLv3+
# SPDX confirmed
License:	GPL-2.0-or-later

%description	utils
This package contains some utility applications based on
%{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains some documentation files for
%{name}.

%prep
%setup -q
%patch -P0 -p1 -b .syspath
%patch -P1 -p1 -b .format

# Honor Fedora compilar flags
touch -r configure.ac{,.timestamp}
sed -i.flags \
	-e '\@^CXXFLAGS=""@d' \
	configure.ac configure
touch -r configure.ac{.timestamp,}

for f in \
	AUTHORS \
	doc/{styles,menu}.css
do
	mv $f{,.iso}
	iconv -f ISO-8859-1 -t UTF-8 -o $f{,.iso}
	touch -r $f{.iso,}
	rm -f $f.iso
done

%build
%configure \
	--disable-static \
%if 0
	--enable-webp \
%endif
	%{nil}
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/lib*.la

# Change Adie.stx path
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_bindir}/Adie.stx %{buildroot}%{_datadir}/%{name}/
chmod 0644 %{buildroot}%{_datadir}/%{name}/Adie.stx

# Make fox-config arch-dependent
mv \
	%{buildroot}/%{_bindir}/fox-config \
	%{buildroot}/%{_bindir}/fox-config.$(arch)
cat > %{buildroot}/%{_bindir}/fox-config <<EOF
#!/bin/sh
exec %{_bindir}/fox-config.\$(arch) \$@
EOF
chmod 0755 %{buildroot}%{_bindir}/fox-config

# Rename too generic names
# Create desktop file for GUI
mkdir -p %{buildroot}%{_libexecdir}/fox
mkdir -p %{buildroot}%{_datadir}/applications
for bin in %{buildroot}%{_bindir}/*
do
	name=$(basename $bin)
	[ "${name%.stx}" = "${name}" ] || continue
	[ "${name#fox-config}" = "${name}" ] || continue
	mv %{buildroot}%{_bindir}/${name} %{buildroot}%{_libexecdir}/fox/
	cat > %{buildroot}%{_bindir}/fox-${name} <<EOF
#!/bin/sh
export PATH=%{_libexecdir}/%{name}:\$PATH
exec ${name} \$@
EOF
	chmod 0755 %{buildroot}%{_bindir}/fox-${name}
	mv %{buildroot}/%{_mandir}/man1/{,fox-}$name.1

	[ "$name" = reswrap ] && continue
	[ "$name" = adie ] && EXTRA_CATEGORY="TextEditor;"
	cat > %{buildroot}%{_datadir}/applications/fox-${name}.desktop <<EOF
[Desktop Entry]
Name=fox-${name}
Comment=${name}
TryExec=fox-${name}
Exec=fox-${name}
Terminal=false
Type=Application
Categories=Utility;$EXTRA_CATEGORY
EOF
	desktop-file-validate %{buildroot}%{_datadir}/applications/fox-${name}.desktop
done

# Move html files to -doc
rm -rf doc-files
mkdir doc-files
mv %{buildroot}%{_docdir}/%{name}-*/html doc-files
rm -f doc-files/html/filter.pl


%check
# Binary files created under tests/ directory are actually GUI test
# program, so nothing can do here.
exit 0

%ldconfig_scriptlets
	
%files
%doc	AUTHORS
%license	LICENSE*
%license	README
%dir	%{_datadir}/%{name}
%{_libdir}/libFOX-1.6.so.*
%{_libdir}/libCHART-1.6.so.*

%files	devel
%doc	ADDITIONS
%doc	TRACING

%{_bindir}/fox-config*
%{_libdir}/pkgconfig/fox.pc
%{_libdir}/libFOX-1.6.so
%{_libdir}/libCHART-1.6.so
%{_includedir}/fox-1.6/

%files	utils
%license	adie/LICENSE

%{_bindir}/fox-*
%exclude	%{_bindir}/fox-config*
%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%{_datadir}/%{name}/*.stx
%{_datadir}/applications/*desktop
%{_mandir}/man1/fox-*

%files	doc
%doc	doc-files/html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.58-1
- 1.6.58

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.57-13
- SPDX migration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.57-7
- bump release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.6.57-6
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun  1 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.57-1
- 1.6.57

* Sun Feb 25 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.56-1
- 1.6.56

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.55-1
- 1.6.55

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May  3 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.54-1
- 1.6.54

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.53-1
- 1.6.53

* Sat Dec  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.52-1
- 1.6.52

* Fri Jun 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.51-1
- 1.6.51

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.50-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.50-1
- Update to 1.6.50

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.49-2
- Fix libCHART.so linkage to erase undefined non-weak symbols
- Fix license tag for stable tarball
- Modify files entry for documentation

* Tue Apr 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.49-1
- Initial packaging
