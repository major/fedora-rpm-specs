%global apiversion 0.3

Name:           libwpg
Version:        0.3.4
Release:        %autorelease
Summary:        A library for import of WordPerfect Graphics images

License:        LGPL-2.1-or-later OR MPL-2.0
URL:            http://libwpg.sourceforge.net/
Source0:        http://download.sourceforge.net/libwpg/%{name}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Std)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  make

%description
%{name} is a library for import of images in WPG
(WordPerfect Graphics) format. WPG is the format used among others in
Corel software, such as WordPerfect and Presentations.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains API documentation for %{name}.

%package tools
Summary:        Tools to convert WordPerfect Graphics images to other formats
# wpg2svgbatch.pl says "GPL", without specifying version, and points to
# http://www.gnu.org/copyleft/gpl.html . I assume this means "any
# version".
License:        (LGPLv2+ or MPLv2.0) and GPL+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to convert WordPerfect Graphics images to other formats. Supported
are: SVG, raw.

%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in wpg2raw wpg2svg; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
help2man -N -S '%{name} %{version}' -n 'batch convert WordPerfect Graphics files into SVG' \
    --help-option=-h --version-string='wpg2svgbatch.pl %{version}' \
    -o wpg2svgbatch.pl.1 ./src/conv/svg/wpg2svgbatch.pl
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 wpg2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%files tools
%{_bindir}/wpg2raw
%{_bindir}/wpg2svg
%{_bindir}/wpg2svgbatch.pl
%{_mandir}/man1/wpg2raw.1*
%{_mandir}/man1/wpg2svg.1*
%{_mandir}/man1/wpg2svgbatch.pl.1*

%changelog
%autochangelog
