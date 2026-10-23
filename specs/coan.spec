Name:		coan
Version:	6.0.1
Release:	%autorelease
Summary:	A command line tool for simplifying the pre-processor conditionals in source code
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://coan2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/coan2/bugs/92/
Patch0:         expression_parser.patch
# https://sourceforge.net/p/coan2/bugs/95/
Patch1:         coan-autoconf-c99.patch
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  perl-Pod-Html
BuildRequires:  autoconf automake

# removed python2 dependencies and asked upstream to port tests to python3
# https://sourceforge.net/p/coan2/bugs/93/

# Regression on other arches with F26 mass rebuild (big endian systems)
# Temporarily exclude them
# https://bugzilla.redhat.com/show_bug.cgi?id=1423293
# checking for big-endian host... yes
# RPM build errors:
# configure: error: Sorry. Coan is buggy on big-endian systems
ExcludeArch:	ppc64 s390x %{ix86}


%description
%{name} (formerly sunifdef) is a software engineering tool for analyzing
pre-processor-based configurations of C or C++ source code. Its principal use
is to simplify a body of source code by eliminating any parts that are
redundant with respect to a specified configuration.

%{name} is most useful to developers of constantly evolving products
with large code bases, where pre-processor conditionals are used to
configure the feature sets, APIs or implementations of different
releases. In these environments the code base steadily
accumulates #ifdef-pollution as transient configuration options become
obsolete. %{name} can largely automate the recurrent task of purging
redundant #if-logic from the code.

%prep
%autosetup -p0

for i in AUTHORS LICENSE.BSD README ChangeLog ; do
    sed -i -e 's/\r$//' $i
done

%build
export CXXFLAGS="-std=c++14 -Wno-deprecated -Wno-deprecated-declarations -fpermissive $RPM_OPT_FLAGS"
autoreconf -vi
%configure
%make_build

# disabling all checks it's broken again on rawhide :(
# some tests are broken in armv7hl and ppc64le - disable until upstream
# fixes the issue upstream bug report:
#     https://sourceforge.net/p/coan2/bugs/83/
# so for now we'll just allow the tests to fail
#
# %ifnarch %{arm} ppc64le
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; false)
# %else
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; true)
# %endif


%install
%make_install

%files
%doc AUTHORS README ChangeLog
%license LICENSE.BSD
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
