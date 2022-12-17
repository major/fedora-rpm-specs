%define    profiledir    %{_sysconfdir}/profile.d

Name:       cdargs
Version:    1.35
Release:    %autorelease
Summary:    The shell cd with bookmarks and browser
License:    GPLv2+
URL:        http://www.skamphausen.de/cgi-bin/ska/CDargs/
Source0:    http://www.skamphausen.de/downloads/cdargs/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}_emacs-init.el

Patch0:     %{name}-%{version}_shebangs.patch
Patch1:     %{name}-%{version}_format_security.patch
Patch2:     %{name}-%{version}_fix_fsf_address.patch
Patch3:     %{name}-%{version}_configure_c99.patch

BuildRequires:    gcc-c++
BuildRequires:    ncurses-devel
BuildRequires:    emacs
BuildRequires:    make
Requires:         emacs-filesystem >= %{_emacs_version}

%description
Enables the user to quickly change working directory by navigating cd arguments
and expanding the shell built-in cd with bookmarks and browser.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build
%{_emacs_bytecompile} contrib/cdargs.el

%install
%make_install

mkdir -p %{buildroot}%{profiledir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}

install -p -m 644 contrib/cdargs.el* %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/cdargs-init.el

install -p -m 644 contrib/cdargs-bash.sh %{buildroot}%{profiledir}/cdargs.sh
install -p -m 644 contrib/cdargs-tcsh.csh %{buildroot}%{profiledir}/cdargs.csh
install -D -p -m 644 src/cdargs.h %{buildroot}%{_includedir}/cdargs.h

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/cdargs
%config(noreplace) %{profiledir}/cdargs.*
%doc %{_mandir}/man1/cdargs.1*
%dir %{_emacs_sitelispdir}/%{name}
%{_emacs_sitelispdir}/%{name}/*.el
%{_emacs_sitelispdir}/%{name}/*.elc
%{_emacs_sitestartdir}/cdargs-init.el

%files devel
%{_includedir}/cdargs.h

%changelog
%autochangelog
