%global sum GNU Scientific Library Interface for python

# Put all the documentation in one place
%global _docdir_fmt %{name}

# A C++ header file is named with a .py extension
%global _python_bytecompile_errors_terminate_build 0

Name:           pygsl
Version:        2.6.3
Release:        %autorelease
Summary:        %{sum}

License:        GPL-2.0-or-later
URL:            https://github.com/pygsl/pygsl
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.gnu.org/software/gsl/doc/html/objects.inv
# Link with flexiblas instead of gslcblas
Patch:          %{name}-flexiblas.patch
# Fix the multinomial rng test
# See https://github.com/pygsl/pygsl/pull/58
Patch:          %{name}-rng-test.patch
# Remove a redundant definition
# https://github.com/pygsl/pygsl/pull/88
Patch:          %{name}-remove-redundant-def.patch

# Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -p
BuildOption(install): -L pygsl

BuildRequires:  gcc
BuildRequires:  gsl-devel
BuildRequires:  flexiblas-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  swig

# Documentation dependencies
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%description
This project provides a python interface for the GNU scientific library (gsl).

%package -n python3-pygsl
Summary:       %{sum}
# This can be removed when F44 reaches EOL
Obsoletes:     pygsl < 2.4.0-2
Provides:      pygsl = %{version}-%{release}

%description -n python3-pygsl
This project provides a python interface for the GNU scientific library (gsl).

%package -n python3-pygsl-devel
Summary:       Development files for pygsl
Requires:      python3-pygsl = %{version}-%{release}
# This can be removed when F44 reaches EOL
Obsoletes:     pygsl-devel < 2.4.0-2
Provides:      pygsl-devel = %{version}-%{release}

%description -n python3-pygsl-devel
Development files for pygsl.

%package doc
Summary:       Reference manual for pygsl
License:       GFDL-1.1-no-invariants-or-later AND GPL-2.0-or-later
BuildArch:     noarch

%description doc
Reference manual for pygsl.

%prep
%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Fix character encodings
mv ChangeLog ChangeLog.orig
iconv -f ISO-8859-1 -t UTF-8 ChangeLog.orig > ChangeLog
fixtimestamp ChangeLog

# Fix end-of-line encodings
for f in api/pygsl.statistics ref/chebyshev ref/const ref/differentiation \
         ref/errors ref/histogram ref/ieee ref/index ref/old/ref_orig \
         ref/panda_rst/copyright ref/panda_rst/install ref/rng ref/sf \
         ref/statistics ref/sum ref-obsolete/copyright ref-obsolete/install \
         ref-obsolete/ref; do
  sed -i.orig 's/\r//g' doc/$f.rst
  fixtimestamp doc/$f.rst
done

sed -i.orig 's/\r//g' doc/win/pygsl_msys2_prepare.sh
fixtimestamp doc/win/pygsl_msys2_prepare.sh

# Use local objects.inv for intersphinx
sed -e "s|\('http://www.gnu.org/software/gsl/doc/html/', \)None|\1'%{SOURCE1}'|" \
    -i doc/conf.py

# Don't invoke python via env
%py3_shebang_fix pygsl typemaps/c.py

# A fix for swig 4.4 broke the build with swig 4.3
swigver=$(ls -1d %{_datadir}/swig/* | cut -d/ -f5)
swigmaj=$(cut -d. -f1 <<< $swigver)
swigmin=$(cut -d. -f2 <<< $swigver)
if [ "$swigmaj" -eq 4 -a "$swigmin" -lt 4 ]; then
    sed -i 's/import_array1(-1)/import_array()/' src/gslwrap/interpolation2d.i
fi

%build -p
# Use flexiblas instead of gslcblas
export GSL_CBLAS_LIB=-lflexiblas

%install -a
# Fix permissions
chmod 0755 %{buildroot}%{python3_sitearch}/pygsl/{_generic_solver,block,chebyshev,fit,gsl_function,integrate,interpolation,minimize,monte,multi{fit{,_nlin},minimize,roots},odeiv,qrng,roots,siman,spline,vector}.py

# Move the header files where we want them
mkdir %{buildroot}%{_includedir}
mv %{buildroot}%{python3_sitearch}/Include \
   %{buildroot}%{_includedir}/python%{python3_version}

# There are no byte-compiled files for non-python files with a py extension
sed -i '\%%cfg/__pycache__%%d' %{pyproject_files}

# Build the documentation once we have an installed tree to reference
%{py3_test_envvars} sphinx-build -b html %{?_smp_mflags} doc html
rst2html --no-datestamp CREDITS.rst CREDITS.html
rst2html --no-datestamp README.rst README.html
rst2html --no-datestamp TODO.rst TODO.html
rm -fr html/.{buildinfo,doctrees}

%check
export FLEXIBLAS=netlib
%pytest tests/

%files -n python3-pygsl -f %{pyproject_files}
%doc ChangeLog README.html CREDITS.html TODO.html
%license COPYING

%files -n python3-pygsl-devel
%{_includedir}/python%{python3_version}/pygsl/

%files doc
%doc examples/ html/
%license COPYING

%changelog
%autochangelog
