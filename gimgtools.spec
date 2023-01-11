%global forgeurl https://github.com/wuyongzheng/gimgtools
%global date 20130918
%global commit 92d015749e105c5fb8eb704ae503a5c7e51af2bd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gimgtools
Version:        0.03^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Garmin Image Tools

License:        GPL-2.0-only
URL:            https://code.google.com/archive/p/gimgtools/
Source:         %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# Fixed Makefile for compile on Mac OS X
Patch:          %{forgeurl}/pull/3.patch
# Add license file for GPLv2
Patch:          %{forgeurl}/pull/7.patch

BuildRequires:  gcc
BuildRequires:  make

%description
gimgtools is a set of command-line tools to examine and manipulate Garmin IMG
(the map format) files.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build \
  CC="$CC" \
  CFLAGS="-Wall -D_FILE_OFFSET_BITS=64 $CFLAGS" \
  LDLIBS="$LDFLAGS -lm"

%install
for bin in cmdc gimgch gimgextract gimginfo gimgfixcmd gimgunlock gimgxor; do
  install -Dpm0755 -t %{buildroot}%{_bindir} "$bin"
done

%files
%license LICENSE
%doc README.txt
%{_bindir}/cmdc
%{_bindir}/gimg*

%changelog
%autochangelog
