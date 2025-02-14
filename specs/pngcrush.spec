%global         _hardened_build 1

Summary:        Optimizer for PNG (Portable Network Graphics) files
Name:           pngcrush
Version:        1.8.13
Release:        %autorelease
License:        Zlib
URL:            http://pmt.sourceforge.net/%{name}/
Source0:        http://downloads.sourceforge.net/pmt/%{name}-%{version}-nolib.tar.xz
# from Debian sid.
Source1:        %{name}.sgml
# Fix building with libpng >= 1.6.42
# https://github.com/glennrp/pmt/pull/2
Patch:          https://patch-diff.githubusercontent.com/raw/glennrp/pmt/pull/2.patch#/pngcrush-1.8.13-fix-undeclared-identifier.patch
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
pngcrush is a commandline optimizer for PNG (Portable Network Graphics) files.
Its main purpose is to reduce the size of the PNG IDAT datastream by trying
various compression levels and PNG filter methods. It also can be used to
remove unwanted ancillary chunks, or to add certain chunks including gAMA,
tRNS, iCCP, and textual chunks. 

%prep
%autosetup -n %{name}-%{version}-nolib
cp %{SOURCE1} . 

%build
%set_build_flags
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h # force using system headers
pngflags=$(pkg-config --cflags --libs libpng)
${CC} %{optflags} $pngflags -lz $RPM_LD_FLAGS -o %{name} %{name}.c
docbook2man %{name}.sgml

%install
%{__install} -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -D -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog.html
%license LICENSE
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
