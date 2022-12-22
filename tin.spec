Name: tin
Version: 2.6.1
Release: %autorelease
Summary: Basic Internet news reader
License: BSD
URL: http://www.tin.org/
Source0: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz
Source1: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz.sign
Source2: tin-pgp-key-0x5A49550EB490B4D1.txt
Patch0: tin-configure-c99.patch
BuildRequires: make
BuildRequires: %{_bindir}/ispell
BuildRequires:  gcc-c++
BuildRequires: gettext
BuildRequires: %{_bindir}/gpg1
BuildRequires: ncurses-devel, byacc, pcre-devel, gnupg2
BuildRequires: perl-generators
BuildRequires: libgsasl-devel
BuildRequires: libicu-devel
BuildRequires: libidn-devel

%description
Tin is a basic, easy to use Internet news reader.  Tin can read news
locally or remotely via an NNTP (Network News Transport Protocol)
server.

Install tin if you need a basic news reader.

%prep
workdir=$(mktemp --directory)
workring=${workdir}/keyring.gpg
gpg1 --homedir=${workdir} --pgp2 --yes --output="${workring}" --dearmor %{S:2}
gpg1 --homedir=${workdir} --pgp2 --verify --keyring="${workring}" %{S:1} %{S:0}
rm -r ${workdir}
%autosetup -p1

%build
%configure \
	--with-libdir=/var/lib/news \
	--with-spooldir=/var/spool/news/articles \
	--enable-nntp \
	--enable-prototypes \
	--disable-echo \
	--disable-mime-strict-charset \
	--enable-color \
	--enable-ncurses \
	--with-screen=ncursesw \
	--enable-locale \
	--with-gpg=%{_bindir}/gpg2 \
	--with-mime-default-charset=UTF-8 \
	--with-pcre

%{__sed} -i -e 's/@\$(INSTALL) -s/@\$(INSTALL)/g' -e 's/@\$(CC)/\$(CC)/g' -e  's/@\$(CPP)/\$(CPP)/g' src/Makefile

%{__make} clean %{?_smp_mflags}
%{__make} build %{?_smp_mflags}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# url_handler.sh conflicts with mutt
%{__rm} -f $RPM_BUILD_ROOT/%{_bindir}/url_handler.pl
# INSTALL file is not needed in the final RPM
%{__rm} -f doc/INSTALL

%find_lang %{name}

%files -f %name.lang
%doc README doc/*
%{_bindir}/tin
%{_bindir}/rtin
%{_bindir}/metamutt
%{_bindir}/opt-case.pl
%{_bindir}/w2r.pl
%{_bindir}/tinews.pl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
%autochangelog
