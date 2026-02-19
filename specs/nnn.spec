Name:       nnn
Version:    5.2
Release:    %autorelease
Summary:    The missing terminal file browser for X

License:    BSD-2-Clause
URL:        https://github.com/jarun/nnn
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  readline-devel

%description
nnn is probably the fastest and most resource-sensitive (with all
its capabilities) file browser you have ever used. It's extremely flexible
too - integrates with your DE and favourite GUI utilities, works with
the desktop opener, supports bookmarks, has smart navigation shortcuts,
navigate-as-you-type mode, disk usage analyzer mode, comprehensive file
details and much more. nnn was initially forked from noice but is
significantly different today.

Cool things you can do with nnn:

 - open any file in the default desktop application or a custom one
 - navigate-as-you-type (search-as-you-type enabled even on directory switch)
 - check disk usage with number of files in current directory tree
 - run desktop search utility (gnome-search-tool or catfish) in any directory
 - copy absolute file paths to clipboard, spawn a terminal and use the paths
 - navigate instantly using shortcuts like ~, -, & or handy bookmarks
 - use cd ..... at chdir prompt to go to a parent directory
 - detailed file stats, media info, list and extract archives
 - pin a directory you may need to revisit and jump to it anytime
 - lock the current terminal after a specified idle time
 - change directory on exit

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i "s|^install: all|install:|" Makefile

%build
%set_build_flags
%make_build STRIP=/bin/true

%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  misc/auto-completion/bash/nnn-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  misc/auto-completion/fish/nnn.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  misc/auto-completion/zsh/_nnn

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nnn-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/nnn.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_nnn

%changelog
%autochangelog
