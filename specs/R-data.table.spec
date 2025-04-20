%global packname data.table
%global packver  1.17.0
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((xts)\\)

# Some dependency loops.
%global with_loop 0

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Extension of `data.frame`

License:          MPL-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-bit64 >= 4.0.0, R-bit >= 4.0.4, R-curl, R-R.utils, R-xts, R-nanotime, R-zoo >= 1.8-1, R-yaml, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(zlib)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-bit64 >= 4.0.0
BuildRequires:    R-bit >= 4.0.4
BuildRequires:    R-curl
BuildRequires:    R-R.utils
BuildRequires:    R-zoo >= 1.8.1
BuildRequires:    R-yaml
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%if %{with_loop}
BuildRequires:    R-xts
BuildRequires:    R-nanotime
%endif

%description
Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
fast add/modify/delete of columns by group using no copies at all, list
columns, friendly and fast character-separated-value read/write. Offers a
natural and flexible syntax, for faster development.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Useless.
rm %{buildroot}%{rlibdir}/%{packname}/cc


%check
# Segfaults?
%ifnarch aarch64 i686
# Workaround /etc/localtime not being a symlink in koji.
export TZ=Etc/UTC
%if %{with_loop}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --no-tests --ignore-vignettes %{packname}
%endif
%endif

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
%{rlibdir}/%{packname}/libs/data_table.so
%{rlibdir}/%{packname}/tests
%dir %{rlibdir}/%{packname}/po
%dir %{rlibdir}/%{packname}/po/en@quot
%dir %{rlibdir}/%{packname}/po/en@quot/LC_MESSAGES
%lang(en@quot) %{rlibdir}/%{packname}/po/en@quot/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/zh_CN
%dir %{rlibdir}/%{packname}/po/zh_CN/LC_MESSAGES
%lang(zh_CN) %{rlibdir}/%{packname}/po/zh_CN/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/es
%dir %{rlibdir}/%{packname}/po/es/LC_MESSAGES
%lang(es) %{rlibdir}/%{packname}/po/es/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/fr
%dir %{rlibdir}/%{packname}/po/fr/LC_MESSAGES
%lang(fr) %{rlibdir}/%{packname}/po/fr/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/pt_BR
%dir %{rlibdir}/%{packname}/po/pt_BR/LC_MESSAGES
%lang(pt_BR) %{rlibdir}/%{packname}/po/pt_BR/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/ru
%dir %{rlibdir}/%{packname}/po/ru/LC_MESSAGES
%lang(ru) %{rlibdir}/%{packname}/po/ru/LC_MESSAGES/*.mo


%files devel
%{rlibdir}/%{packname}/include


%changelog
%autochangelog
