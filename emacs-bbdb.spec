# Note on building bbdb with support for VM: if support for VM in bbdb is
# required, then the source elisp for VM must be installed at build time. If
# support for BBDB is required in VM, then the BBDB source elisp must be present
# at build time. Hence there is a circular BuildRequires and bootstrapping is
# required. The way to do this is (i) build emacs-vm without BuildRequires:
# emacs-bbdb (ii) build emacs-bbdb with BuildRequires: emacs-vm (iii)
# rebuild emacs-vm with BuildRequires: emacs-bbdb.  Or vice versa.
%define vmsupport 1

%define lispdir %{_emacs_sitelispdir}/bbdb

Name:           emacs-bbdb
Version:        3.2.2b
Release:        %autorelease -s 20220729git1b121e9
Epoch:          1
Summary:        A contact management utility for use with Emacs
Summary(sv):    Ett verktyg för att hantera kontakter i Emacs

License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            http://savannah.nongnu.org/projects/bbdb/

# Releases are somewhat sporadic. Using the lates commit seems more
# reliable. The forgemeta macros don't support Savannah. Use the following
# commands to generate the tarball:
#   git clone --depth=1 https://git.savannah.gnu.org/git/bbdb.git
#   tar cJ --exclude=.git --file=bbdb-20201013.tar.xz bbdb
Source0:	bbdb-20220729.tar.xz
Source1:	emacs-bbdb.metainfo.xml
Patch0:		bbdb-3.2-migrate-fix.patch
Patch1:		bbdb-3.2-mh-folder-mode-fix.patch
# https://lists.nongnu.org/archive/html/bbdb-user/2023-03/msg00000.html
Patch2:         bbdb-compiler-warnings.patch

BuildArch:      noarch
BuildRequires:  autoconf automake emacs info texinfo texinfo-tex
BuildRequires:	libappstream-glib

%if %{vmsupport}
BuildRequires:  emacs-vm
%endif
BuildRequires: make

Requires:       emacs(bin) >= %{_emacs_version}

%description 
BBDB is the Insidious Big Brother Database contact manager for GNU
Emacs.  It provides an address book for email and snail mail
addresses, phone numbers and the like.  It can be linked with various
Emacs mail clients (Message and Mail mode, Rmail, Gnus, MH-E, and VM).
BBDB is fully customizable.

%description -l sv
BBDB är kontakthanteraren Insidious Big Brother Database för GNU
Emacs.  Den tillhandahåller en adressbok för e-post och traditionella
postadresser, telefonnummer och liknande.  Den kan kopplas ihop med
olika Emacs-postklienter (Message- och Mail-läge, Rmail, Gnus, MH-E
och VM).  BBDB går att anpassa fullständigt.


%prep 
%autosetup -n bbdb -p 1

%build
./autogen.sh
%if %{vmsupport}
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb --with-vm-dir=%{_emacs_sitelispdir}/vm
%else
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb
%endif

# Note: make %{?_smp_mflags} fails.
make all

%install
make DESTDIR=%{buildroot} install

# Create and install init file
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cat > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/bbdb-init.el << EOF
(require 'bbdb-loaddefs)
EOF

# Adapt to Fedora-specific naming for doc directory.
mv %{buildroot}%{_docdir}/bbdb %{buildroot}%{_pkgdocdir}

# The COPYING file belongs in the license directory instead.
rm %{buildroot}%{_pkgdocdir}/COPYING

# The install creates a dir file, but this has to be done in package
# installation.
rm %{buildroot}%{_infodir}/dir

# The current documentation is just a template, it doesn't contain any real
# documentation.
rm %{buildroot}%{_infodir}/bbdb.info
rm %{buildroot}%{_pkgdocdir}/bbdb.pdf

# Metainfo
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license COPYING
%{_datadir}/bbdb
%{lispdir}/
%{_pkgdocdir}
%{_emacs_sitestartdir}/bbdb-init.el
%{_datadir}/metainfo/%{name}.metainfo.xml


%changelog
%autochangelog
