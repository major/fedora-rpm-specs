Name:           opari2
Version:        2.0.9
Release:        %autorelease
Summary:        An OpenMP runtime performance measurement instrumenter

License:        BSD-3-Clause
URL:            https://www.vi-hps.org/projects/score-p/
Source0:        https://perftools.pages.jsc.fz-juelich.de/cicd/opari2/tags/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
ExcludeArch:    %{ix86}

%description
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.  It surrounds OpenMP directives and runtime library calls with calls
to the POMP2 measurement interface.

OPARI2 will provide you with a new initialization method that allows for
multi-directory and parallel builds as well as the usage of pre-instrumented
libraries. Furthermore, an efficient way of tracking parent-child
relationships was added. Additionally, we extended OPARI2 to support
instrumentation of OpenMP 3.0 tied tasks.


%prep
%autosetup -p1


%build
# I don't immediately see why using %%configure broke the check target
# in 2.0.7, which worked before.  configure fails if we don't pass the
# flags as args, rather than in the environment.
./configure --disable-silent-rules --prefix=%_prefix \
	    CFLAGS="%build_cflags" CXXFLAGS="%build_cxxflags" \
	    LDFLAGS="%build_ldflags" FCFLAGS="%build_fcflags"
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete -print
find %{buildroot}%{_defaultdocdir}/%{name}/example* -name '*.a' -delete -print
# Avoid duplicated filelist with %%doc
cp -p AUTHORS ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}/


%check
make check || ( cat */test-suite.log && exit 1 )


%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_libexecdir}/pomp2-parse-init-regions.awk
%{_includedir}/%{name}/
%{_defaultdocdir}/%{name}/
%{_datadir}/%{name}/


%changelog
%autochangelog
