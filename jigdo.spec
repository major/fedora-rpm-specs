Name:          jigdo
Version:       0.8.2
Release:       %autorelease
Summary:       Ease distribution of large files over the Internet

# Exception is permission to link with OpenSSL
License:       GPL-2.0-only WITH x11vnc-openssl-exception
URL:           https://www.einval.com/~steve/software/jigdo/
Source0:       %{url}download/%{name}-%{version}.tar.xz
Source1:       %{url}download/%{name}-%{version}.tar.xz.sig
Source2:       https://www.einval.com/~steve/pgp/587979573442684E.asc
Source3:       jigdo.desktop
# fix doc SGML sources e.g. for missing end tags
Patch:         %{name}-0.8.1-fix-docs.patch

BuildRequires: bzip2-devel
BuildRequires: curl-devel
BuildRequires: docbook-utils
BuildRequires: gawk
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: libdb-devel
BuildRequires: make
BuildRequires: wget
BuildRequires: zlib-devel
Requires:      wget

%global _description %{expand:
Jigsaw Download (for short jigdo) is a scheme developed primarily to make it
easy to distribute huge filesystem images (e.g. CD (ISO9660) or DVD (UDF)
images) over the internet, but it could also be used for other data which is
awkward to handle due to its size, like audio/video files or large software
packages.

jigdo tries to ensure that the large file is downloaded in small parts which can
be stored on different servers. People who want to download the image do so by
telling the jigdo download tool to process one ".jigdo" file; using it, jigdo
downloads the parts and reassembles the image. jigdo-file is used to prepare the
files for download.}

%description %{_description}


%prep
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# don't clobber -g from C*FLAGS
sed -i '/.*echo "$C.*FLAGS"/d' configure


%build
export LDFLAGS="$LDFLAGS -lpthread"
%configure --with-libdb=-ldb
# make_build
make # not SMP safe


%install
%make_install
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc changelog README THANKS doc/*.html doc/TechDetails.txt doc/README-bindist.txt
%{_bindir}/jigdo-file
%{_bindir}/jigdo-lite
%{_bindir}/jigdo-mirror
%{_datadir}/%{name}
%{_mandir}/man1/jigdo-file.1*
%{_mandir}/man1/jigdo-lite.1*
%{_mandir}/man1/jigdo-mirror.1*


%changelog
%autochangelog
