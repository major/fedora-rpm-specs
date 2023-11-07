Name:           lowdown
Version:        1.0.2
Release:        %autorelease
Summary:        Simple markdown translator

License:        ISC AND BSD-3-Clause AND MIT
URL:            https://kristaps.bsd.lv/lowdown/
%global github_version_tag %(c=%{version}; echo VERSION_$c | tr '.' '_')

Source:         https://github.com/kristapsdz/lowdown/archive/%{github_version_tag}/%{name}-%{version_no_tilde}.tar.gz
Patch:          0001-Makefile-link-lowdown-dynamically-and-lowdown-diff-s.patch
Patch:          0001-Makefile-do-not-ignore-the-return-value-from-tests.patch

BuildRequires:  make
BuildRequires:  gcc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global soversion 3
%global _docdir_fmt %{name}

%description
Lowdown is a Markdown translator producing HTML5, roff documents in the ms and
man formats, LaTeX, gemini, and terminal output.

Beyond traditional Markdown syntax support, lowdown supports the following
Markdown features and extensions:
  * autolinking
  * fenced code
  * tables
  * superscripts
  * footnotes
  * disabled inline HTML
  * "smart typography"
  * metadata
  * commonmark (in progress)
  * definition lists
  * extended attributes
  * task lists

%package libs
Summary:       %{summary} library

%description libs
This package provides the %{summary}.

%package devel
Summary:       %{summary} header files
Requires:      %{name}-libs = %{version}-%{release}

%description devel
This package provides the %{summary}.

%prep
%autosetup -n lowdown-%{github_version_tag} -p1

%build
./configure \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir}
# ensure LDFLAGS is passed correctly
sed -i "s!^LDFLAGS.*!LDFLAGS = $LDFLAGS!" Makefile.configure 

%make_build

%install
%make_install install_lib_common install_shared
chmod 0755 %{buildroot}%{_bindir}/lowdown
ln -fs lowdown %{buildroot}%{_bindir}/lowdown-diff
chmod 0755 %{buildroot}%{_libdir}/liblowdown.so.%{soversion}
find %{buildroot} -type f -exec chmod u+w {} \;

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
  make regress

%files
%_bindir/lowdown
%_bindir/lowdown-diff
%_mandir/man1/lowdown.1*
%_mandir/man1/lowdown-diff.1*
%_mandir/man5/lowdown.5*
%dir %_datadir/lowdown
%dir %_datadir/lowdown/odt
%_datadir/lowdown/odt/styles.xml

%files libs
%_mandir/man3/lowdown.3*
%_mandir/man3/lowdown_*.3*
%{_libdir}/liblowdown.so.%{soversion}
# Libs subpackage is required by all other subpackages, so store the license here.
%doc README.md
%license LICENSE.md

%files devel
%{_includedir}/lowdown.h
%{_libdir}/pkgconfig/lowdown.pc
%{_libdir}/liblowdown.so

%changelog
%autochangelog
