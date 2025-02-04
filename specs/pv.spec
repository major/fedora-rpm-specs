Summary: A tool for monitoring the progress of data through a pipeline
Name: pv
Version: 1.9.31
Release: %autorelease
License: GPL-3.0-or-later
URL: https://www.ivarch.com/programs/pv.shtml

Source0: https://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
Source1: https://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz.txt
Source2: https://www.ivarch.com/personal/public-key.txt

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: gcc
BuildRequires: gettext


%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure
%make_build


%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}         # /usr/bin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1    # /usr/share/man/man1

%make_install
%find_lang %{name}
rm -v ${RPM_BUILD_ROOT}%{_docdir}/%{name}/{COPYING,INSTALL}

%check
make test


%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_docdir}/%{name}
%license docs/COPYING

%changelog
%autochangelog
