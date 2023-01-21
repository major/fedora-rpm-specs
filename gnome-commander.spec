# gcmd plugins uses symbols defined in gcmd binary
%undefine	_strict_symbol_defs_build

%global        EXIV2_REQ             0.14
%global        GLIB_REQ              2.44.0
%global        LIBGSF_REQ            1.12.0
%global        POPPLER_REQ           0.8
%global        TAGLIB_REQ            1.4

%global        mimeedit_rev          1958

%global        use_autotool          0
%global        update_po             0
%global        if_pre                0

%global        use_gcc_strict_sanitize        0

%global        use_release           1
%global        use_gitbare           0

%if 0%{?use_gitbare} < 1
# force
%global        use_release           1
%endif

%global        flagrel               %{nil}
%if            0%{?use_gcc_strict_sanitize} >= 1
%global        flagrel               %{flagrel}.san
%endif

%if 0%{?use_gitbare}
%global        gittardate            20220113
%global        gittartime            1526
%global        gitbaredate           20220109
%global        git_rev               fed9ef1a44cd01b6c1dfb231795e07f5f067de57
%global        git_short             %(echo %{git_rev} | cut -c-8)
%global        git_version           D%{gitbaredate}git%{git_short}

%global        if_pre                1
%endif

%global        shortver              1.14
%global        fullver               %{shortver}.3
%global        mainrel               1

%if 0%{?use_release} >= 1
%global        fedorarel             %{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif
%if 0%{?use_gitbare} >= 1
%global        fedorarel             %{mainrel}.%{git_version}
%endif

%if 0%{?if_pre} > 0
%global        use_autotool          1
%endif
%if 0%{?use_autotool} < 1
%global        update_po             0
%endif

# Patch1 updates configure.in
%global        use_autotool          1

# Autotool seems still needed to avoid build failure
# under doc/ diretory, need investigating
%global        use_autotool          1

Name:          gnome-commander
# Downgrade 3 times, sorry...
Epoch:         4
Version:       %{fullver}
Release:       %{fedorarel}%{flagrel}%{?dist}.2
Summary:       A nice and fast file manager for the GNOME desktop
Summary(pl):   Menadżer plików dla GNOME oparty o Norton Commander'a (TM)
Summary(sv):   GNOME Commander är en snabb och smidig filhanderare för GNOME

License:       GPLv2+
URL:           http://gcmd.github.io/
%if 0%{?use_release}
Source0:       http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{shortver}/%{name}-%{version}%{?extratag:-%extratag}.tar.xz
%endif
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
Source1:       gnome-commander.sh
# Source0 is created from Source2
Source2:       create-gcmd-git-bare-tarball.sh
Source10:      mimeedit-svn%{mimeedit_rev}.sh
Patch1:        gnome-commander-1.6.0-path-fedora-specific.patch

BuildRequires: gcc-c++
%if 0%{?use_gcc_strict_sanitize}
BuildRequires: libasan
BuildRequires: libubsan
%endif

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool

BuildRequires: pkgconfig(exiv2)         >= %{EXIV2_REQ}
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gnome-vfs-2.0)
BuildRequires: pkgconfig(libgsf-1)        >= %{LIBGSF_REQ}
BuildRequires: pkgconfig(poppler-glib)       >= %{POPPLER_REQ}
BuildRequires: pkgconfig(taglib)        >= %{TAGLIB_REQ}
BuildRequires: pkgconfig(unique-1.0)

BuildRequires: libICE-devel
BuildRequires: libSM-devel

BuildRequires: gnome-doc-utils
BuildRequires: perl(XML::Parser)

%if %{use_autotool}
BuildRequires: automake
BuildRequires: flex
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: gnome-common
%endif
BuildRequires: make
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/appstream-util

# %%check
BuildRequires: gtest-devel

Requires:         gnome-vfs2-smb
Requires:         meld
Requires:         gnome-icon-theme-legacy

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop. 
In addition to performing the basic filemanager functions the program is 
also an FTP-client and it can browse SMB-networks.

%description -l cs
GNOME Commander je pěkný a rychlý správce souborů pro GNOME desktop.
Kromě základních funkcí správy souborů je program také
FTP klient a umí procházet SMB sítěmi.

%description -l pl
GNOME Commander to niewielki i wydajny menadżer plików umożliwiający
wykonywanie za pomocą klawiatury wszystkich standardowych operacji na plikach.
Dostępne są również dodatkowe funkcje jak np. obsługa FTP, czy też obsługa
sieci SMB.

%description -l ru
Быстро работающий файловый менеджер для GNOME. Может выполнять большинство
типовых операций с файлами, умеет обнаруживать изменения, внесенные в файлы
другими программами, и автоматически обновлять отображаемый список файлов.
Поддерживает описания файловых структур в формате DND и кодировки MIME.
Реализует на базовом уровне поддержку FTP через GnomeVFS.

%description -l sv
GNOME Commander är en snabb och smidig filhanderare för GNOME.
Utöver att kunna hantera filer på din egen dator så kan programmet även
ansluta till FTP-servrar och SMB-nätverk.

%prep
%if 0%{?use_release}
%setup -q

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{version}-fedora %{git_rev}
cp -a [A-Z]* ..
cp -a doc ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done

%endif

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

%if 0%{?use_release}
cat > .gitignore <<EOF
Makefile.in
*/Makefile.in
*/*/Makefile.in
ChangeLog-*
INSTALL
aclocal.m4
config.guess
config.h.in
config.sub
configure
compile
depcomp
install-sh
ltmain.sh
m4
missing
test-driver
ylwrap
EOF

git add .
git commit -m "base" -q
%endif

%patch1 -p1 -b .path
git commit -m "Apply Fedora specific path configuration" -a
%if 0%{?use_release}
%endif

%if 0%{use_autotool} > 0
( export NOCONFIGURE=1 ; sh autogen.sh )
%endif

%{__sed} -i.pylib \
   -e 's|\$PY_EXEC_PREFIX/lib|%{_libdir}|' \
   configure

%if 0%{?use_gitbare}
pushd ..
%endif

# gzip
#gzip -9 ChangeLog-*

mkdir TMPBINDIR
cd TMPBINDIR
ln -sf /bin/true ./update-mime-database

%if 0%{?use_gitbare}
popd
%endif

%build
export PATH=$(pwd)/TMPBINDIR:$PATH
export BUILD_TOP_DIR=$(pwd)

%set_build_flags
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
%endif

%if 0%{?use_gitbare}
pushd %{name}
%endif

# Install wrapper script, and move binaries to
# %%{_libexecdir}/%%{name}
mkdir _builddir || :

# For debuginfo issue
find . -name \*.cc | while read f
do
   dirn=$(dirname $f)
   %{__cat} $f | %{__sed} -n -e 's|^#line.*[ \t][ \t]*\"\(.*\)"$|\1|p' | \
      sort | uniq | while read g
   do
      %{__mkdir_p} _builddir/$dirn
      %{__cp} -p $dirn/$g _builddir/$dirn
  done
done

pushd _builddir

ln -sf ../configure
%configure \
   --srcdir=$(pwd)/.. \
   --bindir=%{_libexecdir}/%{name} \
   --disable-Werror \
   --disable-scrollkeeper \
   %{nil}

%{__cp} -p README ${BUILD_TOP_DIR}

%if %{update_po}
%{__make} -C po gnome-commander.pot update-po
%endif

# First make po without _smp_mflags, so that messages
# won't be mixed up
# Second doc/, parallel make seems to fail
%{__make} -C po GMSGFMT="msgfmt --statistics"
%{__make} -C doc
%{__make} %{?_smp_mflags} -k

popd # from _builddir

%if 0%{?use_gitbare}
popd
%endif

%install
%{__rm} -rf %{buildroot}

export PATH=$(pwd)/TMPBINDIR:$PATH

%if 0%{?use_gitbare}
pushd %{name}
%endif

pushd _builddir
%{__make} \
   INSTALL="%{__install} -c -p" \
   DESTDIR=%{buildroot} \
   install
popd # from _builddir

# Desktop file
desktop-file-install \
   --delete-original \
   --vendor '' \
   --remove-category Application \
   --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/org.gnome.%{name}.desktop

# Install wrapper
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -cpm 0755 %SOURCE1 %{buildroot}%{_bindir}/%{name}

# install gnome-file-types-properties (bug 458667)
%if 0
%{__install} -cpm 0755 mimeedit.sh \
	%{buildroot}%{_libexecdir}/%{name}/gnome-file-types-properties
%endif

%{__rm} -f %{buildroot}%{_libdir}/%{name}/*.{a,la}
%{__rm} -f %{buildroot}%{_libdir}/%{name}/*/*.{a,la}

%if 0%{?use_gitbare}
popd
%endif

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.%{name}.appdata.xml

%if 0%{?use_gitbare}
pushd %{name}
%endif

pushd _builddir
export ASAN_OPTIONS=detect_leaks=0
make check

%if 0%{?use_gitbare}
popd
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS
%doc BUGS
%doc ChangeLog*
%doc COPYING
%doc NEWS
%doc README
%doc TODO
%doc doc/*.txt

%{_bindir}/*
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%{_datadir}/applications/org.gnome.%{name}.desktop
%{_metainfodir}/org.gnome.%{name}.appdata.xml

%{_datadir}/help/*/%{name}/

%{_datadir}/glib-2.0/schemas/org.gnome.*xml

%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/pixmaps/%{name}/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.14.3-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.14.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.14.3-1
- 1.14.3

* Thu Mar 31 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.14.2-1
- 1.14.2

* Thu Mar  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.14.1-1
- 1.14.1

* Sun Feb  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.14.0-1
- 1.14.0

* Mon Nov 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.3.1-2
- Fix crash when saving device information on preference

* Mon Nov 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.3.1-1
- 1.12.3.1

* Sun Nov 21 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.3-1
- 1.12.3
- enable test

* Fri Aug 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.2-2
- Drop old scrollkeeper stuff

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.2-1.1
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.2-1
- 1.12.2

* Mon Apr 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.1-1
- 1.12.1

* Fri Mar 26 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.12.0-1
- 1.12.0

* Tue Feb 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.3-3
- Fix FTBFS wrt std::byte <=> Exiv2::byte confusion, perhaps exposed by glibc 2.33.9000

* Tue Feb 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.3-2
- Backport upstream patch for opening properties popup by keypress issue
  (upstream bug 96)

* Tue Jun 30 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.3-1
- 1.10.3

* Mon Feb 03 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 4:1.10.2-2
- Rebuild for poppler-0.84.0

* Tue May 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.2-1
- 1.10.2

* Thu May 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.1-1
- 1.10.1

* Wed Apr  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.10.0-1
- 1.10.0

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 4:1.8.1-2
- rebuild (exiv2)

* Tue Mar  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.8.1-1
- 1.8.1

* Thu Feb 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.8.0-2
- Disable -z defs because plugin uses binary internal symbols

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4:1.8.0-1.1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 10 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.8.0-1
- 1.8.0

* Mon May 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.4-1
- 1.6.4

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 4:1.6.3-1.1
- rebuild (exiv2)

* Mon Feb 27 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.3-1
- 1.6.3

* Wed Feb 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.2-2
- F-26: mass rebuild

* Wed Nov  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.2-1
- 1.6.2

* Wed Oct 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.1-1
- 1.6.1

* Sun Oct 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.6.0-1
- 1.6.0

* Sun Sep 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.9-1
- 1.4.9

* Wed Mar 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.8-1
- 1.4.8

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.7-2
- Fix for gcc6 -Werror=format-security

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 4:1.4.7-1.1
- rebuild (exiv2)

* Sun May 31 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.7-1
- 1.4.7

* Thu May 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.6-3
- Select one entry when pattern matched (bgo#749869)

* Wed May 27 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.6-2
- Fix return value on mime_exec_file() (bgo#749833, #745454)
- Some backport fix

* Wed May 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.6-1
- Update to 1.4.6

* Thu May  7 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.5-5.D20150504git5a4806f
- Fix infinite loop when pressing "Enter" on seaching dialog after
  searching is done
  (bug 1190508, GNOME bug 748869)

* Mon May  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.5-4.D20150504git5a4806f
- Try the latest git

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4:1.4.5-3.1
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.5-3
- Fix abort on opening property dialog on directory on ftp server with "odd" uid
  (bug 1200349, GNOME bug 746003)


* Wed Mar 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.5-2
- Require gnome-icon-theme-legacy

* Mon Jan 26 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.5-1
- Update to 1.4.5

* Thu Nov 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.4-1
- Update to 1.4.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:1.4.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.3-1
- Update to 1.4.3

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.2-2
- F-21: mass rebuild

* Mon May 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.2-1
- Update to 1.4.2

* Mon May 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.1-3
- Remove no longer supported mimetype configuration

* Fri Apr 11 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.1-2
- F21 gcc49 rebuild

* Mon Apr 07 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.1-1
- Update to  1.4.1

* Wed Mar 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.0-2
- Fix build error on armv7fl about missing vtable

* Tue Mar 18 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.4.0-1
- Update to 1.4.0

* Tue Jan 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.8.17-1
- Update to 1.2.8.17

* Thu Dec 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.8.16-1
- Update to 1.2.8.16

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4:1.2.8.15-12.1
- rebuild (exiv2)

* Tue Dec  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.8.15-12
- Support -Werror=format-security

* Sat Aug 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.8.15-11
- Patch to compile with poppler 0.24.0

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 4:1.2.18.15-10
- Rebuild (poppler-0.24.0)

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.18.15-9
- F-20: mass rebuild

* Mon Jul  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4:1.2.18.15-8
- F-20: rebuild (poppler)
- Patch to build against libgsf 1.14.26

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.2.8.15-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3:1.2.8.15-8
- Fix additional build error with gcc47

* Fri Jan 18 2013 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.15-7
- Rebuild (poppler-0.22.0)

* Mon Aug  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.15-6
- F-18: Mass rebuild

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.15-5
- Rebuild (poppler-0.20.1)

* Fri May 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.15-4
- Patch to compile with poppler 0.20.0
  (bug 822405: patch by Marek Kašík [mkasik@redhat.com])

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.15-3
- rebuild (exiv2)

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.15-2
- F-17: rebuild against gcc47

* Wed Dec  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.15-1
- Update to 1.2.8.15

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.14-1.2
- rebuild(poppler)

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.14-1.1
- rebuild (exiv2)

* Sun Oct  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.14-1
- Update to 1.2.8.14

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.13-3
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.13-2
- Rebuild (poppler-0.17.3)

* Sun Aug  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.13-1
- Update to 1.2.8.13

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.12-2
- Rebuild (poppler-0.17.0)

* Sat Jun 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.12-1
- Update to 1.2.8.12

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3:1.2.8.11-1
- Update to 1.2.8.11

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 3:1.2.8.10-3
- Rebuild (poppler-0.16.3)

* Mon Feb 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.10-2
- F-15 mass rebuild

* Thu Jan 20 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.10-1
- Update to 1.2.8.10

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.9-1.2
- rebuild (exiv2,poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.9-1.1
- rebuild (poppler)

* Sat Dec  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.9-1
- Update to 1.2.8.9

* Sun Nov 7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-15: rebuild against new poppler

* Sat Oct  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.8-3
- Add more explicit BRs
- F-15: rebuild against newer poppler

* Fri Sep 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.8-1
- Update to 1.2.8.8
- Fix parallel make issue

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 3:1.2.8.7-1.1
- rebuild (poppler)

* Fri Jul 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.7-1
- Update to 1.2.8.7

* Fri Jul 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: rebuild against python 2.7

* Sat Jun 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3:1.2.8.6-1
- Finally downgrade to 1.2.8.6 even on rawhide as the upsteam changed release plan

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 2:1.2.9-0.6.git_D20100215T0000
- rebuild (exiv2)

* Wed May 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Bump Epoch again to keep upgrade path from F-13

* Wed May  5 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2.9-0.4.git_D20100215T0000
- Rebuild against new poppler

* Mon Feb 15 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Again try latest git

* Thu Jan 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.9-0.3.git_D20100114T1630
- Update to the latest git
- Add Requires: gnome-vfs2-smb (from a request from the upstream)

* Mon Jan  4 2010 Rex Dieter <rdieter@fedoraproject.org> 1:1.2.9-0.2
- rebuild (exiv2)

* Fri Jan  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- A Happy New Year

* Thu Dec  3 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest git
  (to fix crash when cancelling symlink creation with ESC
   bug 542366, GNOME bug 603301)

* Thu Nov 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:1.2.9-0.1.git_D20091126T1510
- Chase master git branch for F-13 after discussion with the upstream
  developer

* Thu Nov 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:1.2.8.3-1
- Use stable 1.2.8.x branch for F-12 after discussion with
  the upstream developer

* Mon Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try latest git

* Sat Sep 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.3.git_D20090924T0215_13dev
- Update Russian translation (from mailing list)

* Thu Sep 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try latest git

* Tue Jul 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Mass rebuild

* Tue Jun 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try latest git

* Mon May 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.2.git_D20090524T2355_13dev
- Upstream moved to git

* Sat Apr 11 2009 Mamour Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.1.svn2532_13dev
- rev 2532

* Thu Apr  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.1.svn2502_13dev
- F-12: switch to 1.3 development branch

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-11: Mass rebuild

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org>
- respin (exiv2)

* Thu Dec 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2361

* Sat Dec  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2332
- libtool 2.2 patch went upstream
- "replace_icon" hack seems no longer needed

* Thu Dec  4 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 2330
- Add patch to compile with libtool 2.2
- And also compile with python 2.6

* Mon Oct 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- 1.2.8 branch
- rev 2221

* Wed Aug 13 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.7-4
- More fix for mimeedit.sh to remove potentially unsafe tmpfile
  creation

* Tue Aug 12 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.7-3
- Install mimeedit script pulled from svn to support mime edit
  menu (bug 458667)

* Wed Jul 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.7-2
- F-10+: Fix icon name due to gnome-icon-theme 2.23.x change

* Wed Jul 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.7-1
- 1.2.7

* Wed Jul 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 1901
- Previous workaround removed

* Mon Jul 14 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rev 1874
- Workaround for Decimal offset mode in Hexdump display mode

* Fri Jul 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- try rev 1870
- ja.po is merged upstream

* Wed Jun 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.2.6-3 
- respin for exiv2

* Mon Jun  2 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.6-2
- 1.2.6
- Add patch to compile with GTK 2.13.X

* Sat Mar  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.5-1
- 1.2.5

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Fri Oct  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-4
- Drop yelp dependency

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-3.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-3.dist.1
- License update

* Mon Jun 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-3
- Drop dependency for yelp

* Sat Jun  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-2
- Add missing BR libgsf-devel

* Sat Jun  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-1
- Update to 1.2.4
- Support python chmlib libiptcdata

* Sat Jun  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-7
- Require yelp (#243392)

* Tue Apr 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-6
- Add maintainer, description elements to gnome-commander.xml for
  newer libxslt

* Tue Jan 20 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-5
- Require meld (#225324)

* Thu Jan 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-4
- Don't remove plugins (#222203)

* Thu Jan  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-3
- Explicitly require version-dependent libraries accroding to
  the request from upstream.

* Thu Dec 21 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-2
- Clean up.

* Tue Nov 14 2006 Piotr Eljasiak <epiotr@use.pl>
- fixed Source0 address

* Mon Jul 17 2006 Piotr Eljasiak <epiotr@use.pl>
- added glib dependencies

* Sun May 14 2006 Stephanos Manos <stefmanos@gmail.com>
- Fixed Scrollkeeper database update
        -disabled scrollkeeper update from make
        -added scrollkeeper-database-update in the %%post & %%postun section
- Added %%post & %%postun entries for the desktop file
- Added %%post & %%postun entries for the gtk+ icon cache file

* Sun Apr 9 2006 Piotr Eljasiak <epiotr@use.pl>
- minor cleanups

* Thu Mar 5 2006 Piotr Eljasiak <epiotr@use.pl>
- added OMF files

* Mon Feb 13 2006 Piotr Eljasiak <epiotr@use.pl>
- install gnome-commander icon to %%{_datadir}/pixmaps/
- install gnome-commander.1* to %%{_mandir}/man1/

* Sat Feb 11 2006 Piotr Eljasiak <epiotr@use.pl>
- set default srcext to .bz2

* Fri Jan 28 2005 Piotr Eljasiak <epiotr@use.pl>
- fixed typo: rpm --> rpmbuild

* Mon May 03 2004 Piotr Eljasiak <epiotr@use.pl>
- converted spec file to utf-8
- used RPM macros a bit more

* Thu Jun 19 2003 Piotr Eljasiak <epiotr@use.pl>
- added libraries

* Tue Mar 25 2003 Piotr Eljasiak <epiotr@use.pl>
- updated Sources

* Mon Jan 20 2003 Piotr Eljasiak <epiotr@use.pl>
- added build dependencies

* Fri Jan 10 2003 Piotr Eljasiak <epiotr@use.pl>
- added localization

* Thu Jan 09 2003 Piotr Eljasiak <epiotr@use.pl>
- added dependencies

* Mon Jun 24 2002 Piotr Eljasiak <epiotr@use.pl>
- more cleanup in install section

* Sat Jun 15 2002 Piotr Eljasiak <epiotr@use.pl>
- simplified install and files sections

* Mon Jun 10 2002 Piotr Eljasiak <epiotr@use.pl>
- .spec file is now generated from .spec.in

* Mon Jun 10 2002 Marcus Bjurman <marbj499@student.liu.se>
- The default icon for this project is now called gnome-commander.png
  The xpm variant of the same icon is now also renamed in the same manner.

* Sat Mar  9 2002 Marcus Bjurman <marbj499@student.liu.se>
- Pumped up the version nr

* Sun Nov  4 2001 Marcus Bjurman <marbj499@student.liu.se>
- Initial build.
