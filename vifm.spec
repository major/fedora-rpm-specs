%bcond_with     gtk
%bcond_without  libmagic
%bcond_with     x11

%global tarball_version %%(echo %{version} | tr '~' '-')

Name:           vifm
Version:        0.13
Release:        %autorelease
Summary:        Vifm is a file manager with curses interface

License:        GPLv2+
URL:            http://vifm.info/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{tarball_version}/%{name}-%{tarball_version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
%if %{with gtk}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
%if %{with libmagic}
BuildRequires:  file-devel
%endif
%if %{with x11}
BuildRequires:  libX11-devel
%endif

Requires:       hicolor-icon-theme

%description
Vifm is a curses based Vim-like file manager extended with some useful ideas
from mutt. If you use Vim, Vifm gives you complete keyboard control over your
files without having to learn a new set of commands. It goes not just about
Vim-like keybindings, but also about modes, options, registers, commands and
other things you might already like in Vim.

Just like Vim, Vifm tries to adhere to the Unix philosophy. So instead of
working solutions which are set in stone user is provided with a set of means
for customization of Vifm to one's likings. Though builtin functionality
should be enough for most of use cases.


%prep
%autosetup -n %{name}-%{tarball_version}


%build
%configure \
%if %{with gtk}
    --with-gtk=yes \
%else
    --with-gtk=no \
%endif
%if %{with libmagic}
    --with-libmagic=yes \
%else
    --with-libmagic=no \
%endif
%if %{with x11}
    --with-X11=yes
%else
    --with-X11=no
%endif
%make_build


%install
%make_install

# Handle license file via regular RPM macros
rm %{buildroot}%{_pkgdocdir}/COPYING


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-convert-dircolors
%{_bindir}/%{name}-pause
%{_bindir}/%{name}-screen-split
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/*
%{_pkgdocdir}/
%{_sysconfdir}/%{name}/


%changelog
%autochangelog
