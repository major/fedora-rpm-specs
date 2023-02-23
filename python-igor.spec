%global gitcommit 2c2a79d85508c8988b6d4ecfd4d0f55cff35ef11
%global gitdate 20150408
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           python-igor
Version:        0.3
Release:        %autorelease
Summary:        Parser for Igor Binary Waves (.ibw) and Packed Experiment (.pxp) files

# igor-0.2/igor/igorpy.py is PD, the restis LGPLv3+
License:        LGPLv3+ and Public Domain

URL:            http://blog.tremily.us/posts/igor/
Source0:        https://github.com/wking/igor/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          adapt-doctests-for-Python-3.8-and-newer-Numpy.patch
Patch:          0001-Avoid-syntax-warning-with-python3.8.patch
Patch:          0002-Remove-use-of-deprecated-method.patch
Patch:          https://github.com/AFM-analysis/igor2/commit/285bef17018bf89e0e09773a3ab32ea38e4231b6.patch

BuildArch:      noarch
BuildRequires:  /usr/bin/rename
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib
BuildRequires:  python3-nose

%description
Python parsers for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics’ IGOR Pro software.

Note that this package is unrelated to igor (Automated distribution
life-cycle testing).

%package -n python3-igor
Summary:        %{summary}
Requires:       python3-numpy
Requires:       python3-matplotlib
Obsoletes:      python2-igor < 0.3-9
%{?python_provide:%python_provide python3-igor}

%description -n python3-igor
Python parsers for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics’ IGOR Pro software.

Note that this package is unrelated to igor (Automated distribution
life-cycle testing).

%prep
%autosetup -p1 -n igor-%{version}

%build
%py3_build

%install
%py3_install

%py3_shebang_fix %{buildroot}%{_bindir}/*.py
rename '.py' '' %{buildroot}%{_bindir}/*

%check
nosetests-%{python3_version} --with-doctest --doctest-tests igor test -v

%global _docdir_fmt %{name}

# make sure that we got the python version right in the header
head -n1 %{buildroot}%{_bindir}/igorbinarywave | grep %{__python3} -q
head -n1 %{buildroot}%{_bindir}/igorpackedexperiment | grep %{__python3} -q

%files -n python3-igor
%{python3_sitelib}/*
%license COPYING.LESSER
%doc README
%{_bindir}/igorbinarywave
%{_bindir}/igorpackedexperiment

%changelog
%autochangelog
