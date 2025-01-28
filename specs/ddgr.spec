Name:       ddgr
Version:    2.2
Release:    %autorelease
Summary:    DuckDuckGo from the terminal

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/ddgr
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  python3-devel


%description
ddgr is a cmdline utility to search DuckDuckGo from the terminal.
While googler is highly popular among cmdline users, in many forums the need
of a similar utility for privacy-aware DuckDuckGo came up. DuckDuckGo Bangs
are super-cool too! So here's ddgr for you!

Unlike the web interface, you can specify the number of search results you
would like to see per page. It's more convenient than skimming through
30-odd search results per page. The default interface is carefully
designed to use minimum space without sacrificing readability.

ddgr isn't affiliated to DuckDuckGo in any way.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i "s|\tinstall -|\t\$(INSTALL) -|" Makefile
sed -i '1s/env //' ddgr


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/ddgr-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  auto-completion/fish/ddgr.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_ddgr


%check
make test


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/ddgr-completion.bash
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ddgr.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_ddgr


%changelog
%autochangelog
