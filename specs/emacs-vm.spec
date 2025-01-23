# Font-lock support of message bodies was added (Source1) from 
# http://de.geocities.com/ulf_jasper/emacs.html on 10th February 2007.

# Note on building VM with support for bbdb: if support for VM in BBDB is
# required, then the source elisp for VM must be installed at build time. If
# support for BBDB is required in VM, then the BBDB source elisp must be present
# at build time. Hence there is a circular BuildRequires and bootstrapping is
# required. The way to do this is (i) build emacs-vm without BuildRequires:
# emacs-bbdb (ii) build emacs-bbdb with BuildRequires: emacs-vm (iii)
# rebuild emacs-vm with BuildRequires: emacs-bbdb. Or vice versa.
%global bbdbsupport 1

%global pkgdir %{_emacs_sitelispdir}/vm
%global etcdir %{_datadir}/emacs/vm
%global pixmapdir %{etcdir}/pixmaps
%global initfile %{_emacs_sitestartdir}/vm-init.el

Summary: Emacs VM mail reader
Summary(sv): Emacs postläsare VM
Name: emacs-vm
%global forgeurl https://gitlab.com/emacs-vm/vm/
%global version0 8.3.0
%global commit c3bc5151c9211eedc4b87549348eea4f57247953
%forgemeta
Version: %forgeversion -p
Release: %autorelease
License: GPL-1.0-or-later AND GPL-2.0-or-later
URL: %forgeurl
Source0: %forgesource
Source1: emacs-vm.metainfo.xml
# https://bugs.launchpad.net/vm/+bug/1225162/comments/6
Patch: marker-pointer.patch

Requires: emacs(bin) >= %{_emacs_version}
BuildArch: noarch
BuildRequires: autoconf
BuildRequires: emacs texinfo texinfo-tex
BuildRequires: libappstream-glib
BuildRequires: make

%if %{bbdbsupport}
BuildRequires: emacs-bbdb
Requires: emacs-bbdb
%endif

%description
VM (View Mail) is an Emacs subsystem that allows e-mail to be read
and disposed of within Emacs.  Commands exist to do the normal things
expected of a mail user agent, such as generating replies, saving
messages to folders, deleting messages and so on.  There are other
more advanced commands that do tasks like bursting and creating
digests, message forwarding, and organizing message presentation
according to various criteria. 

%description -l sv
VM (View Mail) är ett undersystem för Emacs som gör att e-post
kan läsas och hanteras inifrån Emacs.  Det finns kommandon för att
göra de vanliga sakerna som förväntas av ett postprogram, såsom skapa
svar, spara meddelanden till mappar, radera meddelanden och så vidare.
Det finns andra mer avancerade kommandon som gör saker som att
splittra upp eller skapa sammandrag, vidarebefordra meddelanden och
organisera presentationen av meddelanden enligt olika kriterier.

%prep
%forgesetup

%build
autoupdate
autoconf
%configure --with-etcdir=%{etcdir} --with-docdir=%{_pkgdocdir}
make

%install
make install DESTDIR=%{buildroot}

# Create initialization file.
install -d %{buildroot}/%{_emacs_sitestartdir}
echo "(require 'vm-autoloads)" > %{buildroot}/%{initfile}
# Metainfo
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%doc README.headers-only
%doc %{_infodir}/*
%license COPYING
%{pkgdir}
%{etcdir}
%{_pkgdocdir}/*
%{initfile}
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
%autochangelog
