%global packname  pbdZMQ
%global packver   0.3-13
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.13
Release:          %autorelease
Summary:          Programming with Big Data -- Interface to ZeroMQ

License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# https://github.com/snoweye/pbdZMQ/pull/38
Patch0001:        fix-configure.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    zeromq-devel >= 4.0.4

%description
'ZeroMQ' is a well-known library for high-performance asynchronous
messaging in scalable, distributed applications.  This package provides
high level R wrapper functions to easily utilize 'ZeroMQ'. We mainly focus
on interactive client/server programming frameworks.


%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
    --configure-args="--disable-internal-zmq"
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# ZeroMQ copyright is installed even though internal build is disabled.
rm -r %{buildroot}%{rlibdir}/%{packname}/zmq_copyright


%check
%{_bindir}/R CMD check %{packname}


%files
%license %{packname}/COPYING
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%dir %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/etc/Makeconf
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/libs


%changelog
%autochangelog
