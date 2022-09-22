Name:           id3v2
Version:        0.1.12
Release:        %autorelease
Summary:        Command line ID3 tag editor

# See http://sourceforge.net/tracker/index.php?func=detail&aid=1768045&group_id=4193&atid=104193
License:        GPLv2+
URL:            http://id3v2.sourceforge.net/

# Source0:        http://downloads.sourceforge.net/id3v2/%{name}-%{version}.tar.gz
# Run "id3v2-fix-release-tarball.sh id3v2-0.1.12.tar.gz" to remove binaries
# and ".git/" from the tarball and get id3v2-0.1.12-fedora.tar.gz
# Source1:      %{name}-fix-release-tarball.sh
Source0:        %{name}-%{version}-fedora.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  id3lib-devel
BuildRequires: make

%description
id3v2 is a command line tool to add, modify, remove, or view ID3v2
tags, as well as convert or list ID3v1 tags.  ID3 tags are commonly
embedded in compressed music files and are the standard way to more
fully describe the work than would normally be allowed by putting the
information in the filename.


%prep
%setup -q -n %{name}-%{version}-fedora


%build
CXXFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags} PREFIX="%{_prefix}"


%install
install -Dpm 755 id3v2 $RPM_BUILD_ROOT%{_bindir}/id3v2
install -Dpm 644 id3v2.1 $RPM_BUILD_ROOT%{_mandir}/man1/id3v2.1


%files
%license COPYING
%doc README
%{_bindir}/id3v2
%{_mandir}/man1/id3v2.1*


%changelog
%autochangelog
