%global version_base 3.7.0
%dnl %global gitnum 120
%dnl %global githash 1a0b1ae238e1deb132a0ae4a8d0c589d583cc5b0
%dnl %global githashshort %{lua:print(string.sub(rpm.expand('%{githash}'), 1, 11))}

Name:           fish
Version:        %{version_base}%{?gitnum:^%{gitnum}g%{githashshort}}
Release:        %autorelease
Summary:        Friendly interactive shell
# see also doc_src/license.rst
# GPLv2
#   - src/fish.cpp
#   and rest…
# GPLv2+
#   - src/builtins/printf.cpp
# BSD
#   - src/fallback.cpp
#   - share/tools/create_manpage_completions.py
# ISC
#   - src/env.cpp
#   - src/utf8.cpp
#   - src/utf8.h
# LGPLv2+
#   - src/wgetopt.cpp
#   - src/wgetopt.h
# MIT
#   - share/completions/grunt.fish
#   - share/tools/web_config/js/angular-route.js
#   - share/tools/web_config/js/angular-sanitize.js
#   - share/tools/web_config/js/angular.js
# PSF-2.0
#   - doc_src/python_docs_theme/,
License:        GPL-2.0-only AND BSD-3-Clause AND ISC AND LGPL-2.0-or-later AND MIT AND PSF-2.0
URL:            https://fishshell.com
%if %{undefined gitnum}
Source0:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-003837986104878835FA516D7A67D962D88A709A.gpg
%else
Source0:        https://github.com/fish-shell/fish-shell/archive/%{githash}/%{name}-%{githash}.tar.gz
%endif

BuildRequires:  cmake >= 3.5
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3-pexpect
BuildRequires:  procps-ng
BuildRequires:  glibc-langpack-en
%global __python %{__python3}
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  /usr/bin/desktop-file-validate

# tab completion wants man-db
Recommends:     man-db
Recommends:     man-pages
Recommends:     groff-base

Provides:       bundled(js-angular) = 1.8.2

%description
fish is a fully-equipped command line shell (like bash or zsh) that is
smart and user-friendly. fish supports powerful features like syntax
highlighting, autosuggestions, and tab completions that just work, with
nothing to learn or configure.

%prep
%if %{undefined gitnum}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1 %{?gitnum:-n fish-shell-%{githash}}
%if %{defined gitnum}
echo "%{version_base}-%{gitnum}g%{githashshort}" > version
%endif

# Change the bundled scripts to invoke the python binary directly.
for f in $(find share/tools -type f -name '*.py'); do
    sed -i -e '1{s@^#!.*@#!%{__python3}@}' "$f"
done

%build
%cmake -GNinja \
    -DBUILD_DOCS=ON \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -Dextra_completionsdir=%{_datadir}/%{name}/vendor_completions.d \
    -Dextra_functionsdir=%{_datadir}/%{name}/vendor_functions.d \
    -Dextra_confdir=%{_datadir}/%{name}/vendor_conf.d

%cmake_build -t all doc fish_tests

# We still need to slightly manually adapt the pkgconfig file and remove
# some /usr/local/ references (RHBZ#1869376)
sed -i 's^/usr/local/^/usr/^g' %{_vpath_builddir}/*.pc

%install
%cmake_install

# No more automagic Python bytecompilation phase 3
# * https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/tools/

# Install docs from tarball root
cp -a README.rst %{buildroot}%{_pkgdocdir}
cp -a CONTRIBUTING.rst %{buildroot}%{_pkgdocdir}

%find_lang %{name}

%check
# Sadly, ctest is broken
%ninja_build -C %{_vpath_builddir} test
desktop-file-validate %{buildroot}%{_datadir}/applications/fish.desktop

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/fish" > %{_sysconfdir}/shells
    echo "/bin/fish" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/fish$" %{_sysconfdir}/shells || echo "%{_bindir}/fish" >> %{_sysconfdir}/shells
    grep -q "^/bin/fish$" %{_sysconfdir}/shells || echo "/bin/fish" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/fish$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/fish$!d' %{_sysconfdir}/shells
fi

%files -f %{name}.lang
%license COPYING
%{_mandir}/man1/fish*.1*
%{_bindir}/fish*
%config(noreplace) %{_sysconfdir}/fish/
%{_datadir}/fish/
%{_datadir}/pkgconfig/fish.pc
%{_pkgdocdir}
%{_datadir}/applications/fish.desktop
%{_datadir}/pixmaps/fish.png

%changelog
%autochangelog
