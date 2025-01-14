%global packname systemfonts
%global packver  1.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          System Native Font Finding

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Add a missing #include to fix GCC 15 build.
Patch:            https://github.com/r-lib/systemfonts/commit/5f14aef17d13d28d0c039f13e73bb78639ae8674.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-lifecycle
# Suggests:  R-covr, R-knitr, R-rmarkdown, R-testthat >= 2.1.0, R-tools
# LinkingTo: R-cpp11 >= 0.2.1
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-lifecycle
BuildRequires:    R-cpp11-devel >= 0.2.1
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-tools
BuildRequires:    pkgconfig(fontconfig)
BuildRequires:    pkgconfig(freetype2)

%description
Provides system native access to the font catalogue. As font handling
varies between systems it is difficult to correctly locate installed fonts
across different operating systems. The 'systemfonts' package provides
bindings to the native libraries on Windows, macOS and Linux for finding
font files that can then be used further by e.g. graphic devices. The main
use is intended to be from compiled code but 'systemfonts' also provides
access from R.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%autopatch -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION

chmod -x src/*.* src/unix/*.*
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/unfont.ttf

%files devel
%{rlibdir}/%{packname}/include


%changelog
%autochangelog
