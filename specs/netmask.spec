Name:           netmask

%global forgeurl https://github.com/tlby/netmask
%global version0 2.5.0
%forgemeta
Version:        %forgeversion
Release:        %autorelease
Summary:        Utility for determining network masks
Summary(sv):    Verktyg för att bestämma nätverksmasker

License:        GPL-2.0-or-later
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  texinfo


%description
This is a handy tool for generating terse netmasks in several common
formats.  If you've ever maintained a firewall with more than a few
rules in it, you might use netmask to clean up and generalize sloppy
rules left by the network administrator before you.  It will also
convert netmasks from one format to another for the day you change
your firewall software.

%description -l sv
Detta är ett praktiskt verktyg för att generera kortfattade nätmasker
i många vanliga format. Om man någon gång har skött en brandvägg med
mer än några få regler i den, kan man använda netmask för att städa
upp och generalisera slarviga regler som lämnats av
nätverksadministratören före dig. Det kan också konvertera nätmasker
från ett format till ett annat den dag man byter ut programvara för
brandväggen.


%prep
%autosetup


%build
aclocal
autoheader
automake --add-missing
autoconf
%configure
%make_build


%install
%make_install


%check
make check


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/netmask
%{_mandir}/man1/netmask.1*
%exclude %{_infodir}/dir
%{_infodir}/netmask.info*


%changelog
%autochangelog
