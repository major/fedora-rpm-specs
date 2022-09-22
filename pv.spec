Summary: A tool for monitoring the progress of data through a pipeline
Name: pv
Version: 1.6.20
Release: %autorelease
License: Artistic 2.0
Source0: http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
URL: http://www.ivarch.com/programs/pv.shtml


BuildRequires: make
BuildRequires:  gcc
BuildRequires: gettext


%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.


%prep
%setup -q
%ifarch ppc64le
# This test failed on ppc64le https://github.com/a-j-wood/pv/issues/51
rm -v tests/019-remote-cksum
%endif
mv README README.iso8859
iconv -f ISO-8859-1 -t UTF-8 README.iso8859  > README
mv doc/NEWS doc/NEWS.iso8859
iconv -f ISO-8859-1 -t UTF-8 doc/NEWS.iso8859 > doc/NEWS

%build
%configure
%make_build


%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}         # /usr/bin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1    # /usr/share/man/man1

%make_install
%find_lang %{name}


%check
make test


%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%license doc/COPYING
%doc README doc/NEWS doc/TODO


%changelog
%autochangelog
