# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gnatcoll-bindings
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           gnatcoll-bindings
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        The GNAT Components Collection – bindings
Summary(sv):    GNAT Components Collection – bindningar

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later AND GPL-2.0-or-later
# The subpackages have different licenses. This is the aggregation of those.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  gcc-gnat gcc-c++ gprbuild sed dos2unix
# A fedora-gnat-project-common that contains the new GPRinstall macro.
BuildRequires:  fedora-gnat-project-common >= 3.21

BuildRequires:  gnatcoll-core-devel = %{epoch}:%{version}
# Although it's not explicitly stated, I guess it's best to keep all the parts
# of Gnatcoll on the same version number.

BuildRequires:  gmp-devel
BuildRequires:  xz-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
This is the bindings module of the GNAT Components Collection. It provides
bindings to GMP, Iconv, LZMA, Python 3, Readline, Syslog and ZLib, and a
parallel sorting algorithm using OpenMP.

%description -l sv
Detta är bindningsmodulen i GNAT Components Collection. Den tillhandahåller
bindningar till GMP, Iconv, LZMA, Python 3, Readline, Syslog och ZLib, samt en
parallell sorteringsalgoritm som använder OpenMP.


#################
## Subpackages ##
#################

%package devel
Summary:        Development metapackage for the GNAT Components Collection – bindings
Summary(sv):    Metapaket för programmering med GNAT Components Collection – bindningar
Requires:       gnatcoll-gmp-devel      = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-iconv-devel    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-readline-devel = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-syslog-devel   = %{epoch}:%{version}-%{release}
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%description devel
Each binding in the GNAT Components Collection now has its own development
package. This meta-package exists to prevent problems when Fedora is upgraded.
It pulls in those development packages that were previously combined as
gnatcoll-bindings-devel.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv
Varje bindning i GNAT Components Collection har nu ett eget programmeringspaket.
Detta metapaket är till för att undvika problem när Fedora uppgraderas. Det drar
in de programmeringspaketen som förut ingick i gnatcoll-bindings-devel.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.


%package -n gnatcoll-cpp
Summary:        The GNAT Components Collection – C++ binding
Summary(sv):    GNAT Components Collection – C++-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-cpp
This is the C++ component of the GNAT Components Collection. It is an interface
to the C++ ISO/IEC 14882:1998(E) string class.

%description -n gnatcoll-cpp -l sv
Detta är C++-komponenten i GNAT Components Collection. Den är ett gränssnitt
till C++-strängklassen i ISO/IEC 14882:1998(E).


%package -n gnatcoll-cpp-devel
Summary:        Development files for the GNAT Components Collection – C++ binding
Summary(sv):    Filer för programmering med GNAT Components Collection – C++-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-cpp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-cpp-devel
This package contains source code and linking information for developing
applications that use the C++ component of the GNAT Components Collection.
It is an interface to the C++ ISO/IEC 14882:1998(E) string class.

%description -n gnatcoll-cpp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder C++-komponenten i GNAT Components Collection.
Den är ett gränssnitt till C++-strängklassen i ISO/IEC 14882:1998(E).


%package -n gnatcoll-gmp
Summary:        The GNAT Components Collection – GMP binding
Summary(sv):    GNAT Components Collection – GMP-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later
# The Ada files of gnatcoll-gmp are GPLv3+ with exceptions but the C files are
# GPLv2+.

%description -n gnatcoll-gmp
This is the GMP component of the GNAT Components Collection. It is an interface
to the GNU Multiple Precision (GMP) arithmetic library.

%description -n gnatcoll-gmp -l sv
Detta är GMP-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket GNU Multiple Precision (GMP) för godtyckligt precisa
beräkningar.


%package -n gnatcoll-gmp-devel
Summary:        Development files for the GNAT Components Collection – GMP binding
Summary(sv):    Filer för programmering med GNAT Components Collection – GMP-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later
# The Ada files of gnatcoll-gmp are GPLv3+ with exceptions but the C files are
# GPLv2+.
Requires:       gnatcoll-gmp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-gmp-devel
This package contains source code and linking information for developing
applications that use the GMP component of the GNAT Components Collection.
It is an interface to the GNU Multiple Precision (GMP) arithmetic library.

%description -n gnatcoll-gmp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder GMP-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket GNU Multiple Precision (GMP) för
godtyckligt precisa beräkningar.


%package -n gnatcoll-iconv
Summary:        The GNAT Components Collection – Iconv binding
Summary(sv):    GNAT Components Collection – Iconvbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-iconv
This is the Iconv component of the GNAT Components Collection. It is an
interface to libiconv for conversion between character encodings.

%description -n gnatcoll-iconv -l sv
Detta är Iconv-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket Iconv för omvandling mellan teckenkodningar.


%package -n gnatcoll-iconv-devel
Summary:        Development files for the GNAT Components Collection – Iconv binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Iconvbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-iconv%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-iconv-devel
This package contains source code and linking information for developing
applications that use the Iconv component of the GNAT Components Collection.
It is an interface to libiconv for conversion between character encodings.

%description -n gnatcoll-iconv-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Iconv-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket Iconv för omvandling mellan
teckenkodningar.


%package -n gnatcoll-lzma
Summary:        The GNAT Components Collection – LZMA binding
Summary(sv):    GNAT Components Collection – LZMAbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-lzma
This is the LZMA component of the GNAT Components Collection. It is an
interface to liblzma, a library for lossless data compression.

%description -n gnatcoll-lzma -l sv
Detta är LZMA-komponenten i GNAT Components Collection. Den är en gränssnitt
mot biblioteket liblzma för förlustfri datakomprimering.


%package -n gnatcoll-lzma-devel
Summary:        Development files for the GNAT Components Collection – LZMA binding
Summary(sv):    Filer för programmering med GNAT Components Collection – LZMAbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-lzma%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-lzma-devel
This package contains source code and linking information for developing
applications that use the LZMA component of the GNAT Components Collection.
It is an interface to liblzma, a library for lossless data compression.

%description -n gnatcoll-lzma-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder LZMA-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket liblzma för förlustfri datakomprimering.


%package -n gnatcoll-omp
Summary:        The GNAT Components Collection – parallel sorting
Summary(sv):    GNAT Components Collection – parallell sortering
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-omp
This is the OpenMP component of the GNAT Components Collection. It provides a
parallel sorting algorithm using OpenMP.

%description -n gnatcoll-omp -l sv
Detta är OpenMP-komponenten i GNAT Components Collection. Den tillhandahåller
en parallell sorteringsalgoritm som använder OpenMP.


%package -n gnatcoll-omp-devel
Summary:        Development files for the GNAT Components Collection – parallel sorting
Summary(sv):    Filer för programmering med GNAT Components Collection – parallell sortering
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-omp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-omp-devel
This package contains source code and linking information for developing
applications that use the OpenMP component of the GNAT Components Collection.
It provides a parallel sorting algorithm using OpenMP.

%description -n gnatcoll-omp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder OpenMP-komponenten i GNAT Components Collection.
Den tillhandahåller en parallell sorteringsalgoritm som använder OpenMP.


%package -n gnatcoll-python3
Summary:        The GNAT Components Collection – Python 3 binding
Summary(sv):    GNAT Components Collection – Pythonbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
# The license is GPLv3+ with the GCC runtime exception, except for:
# - python3/python_support.c : GPLv3+ (runtime exception not granted).

%description -n gnatcoll-python3
This is the Python 3 component of the GNAT Components Collection. It is an
interface to the Python 3 interpreter.

%description -n gnatcoll-python3 -l sv
Detta är Python 3-komponenten i GNAT Components Collection. Den är ett
gränssnitt mot pythontolken.


%package -n gnatcoll-python3-devel
Summary:        Development files for the GNAT Components Collection – Python 3 binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Pythonbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
# The license is GPLv3+ with the GCC runtime exception, except for:
# - python3/python_support.c : GPLv3+ (runtime exception not granted).
Requires:       gnatcoll-python3%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-python3-devel
This package contains source code and linking information for developing
applications that use the Python 3 component of the GNAT Components Collection.
It is an interface to the Python 3 interpreter.

%description -n gnatcoll-python3-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Python 3-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot pythontolken.


%package -n gnatcoll-readline
Summary:        The GNAT Components Collection – Readline binding
Summary(sv):    GNAT Components Collection – Readlinebindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
# gnatcoll-readline.ads grants the GCC Runtime Library Exception but
# gnatcoll-readline.adb does not, and Readline itself is GPLv3+ without
# exceptions anyway.

%description -n gnatcoll-readline
This is the Readline component of the GNAT Components Collection. It is an
interface to the Readline library for interactive input from the user.

%description -n gnatcoll-readline -l sv
Detta är Readline-komponenten i GNAT Components Collection. Den är ett
gränssnitt mot biblioteket Readline för interaktiv inmatning från användaren.


%package -n gnatcoll-readline-devel
Summary:        Development files for the GNAT Components Collection – Readline binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Readlinebindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
Requires:       gnatcoll-readline%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-readline-devel
This package contains source code and linking information for developing
applications that use the Readline component of the GNAT Components Collection.
It is an interface to the Readline library for interactive input from the user.

%description -n gnatcoll-readline-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Readline-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket Readline för interaktiv inmatning från
användaren.


%package -n gnatcoll-syslog
Summary:        The GNAT Components Collection – Syslog binding
Summary(sv):    GNAT Components Collection – Syslogbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-syslog
This is the Syslog component of the GNAT Components Collection. It is an
interface to the system logger on Unix-like systems.

%description -n gnatcoll-syslog -l sv
Detta är Syslog-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot Unixlika operativsystems loggfunktion.


%package -n gnatcoll-syslog-devel
Summary:        Development files for the GNAT Components Collection – Syslog binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Syslogbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-syslog%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-syslog-devel
This package contains source code and linking information for developing
applications that use the Syslog component of the GNAT Components Collection.
It is an interface to the system logger on Unix-like systems.

%description -n gnatcoll-syslog-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Syslog-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot Unixlika operativsystems loggfunktion.


%package -n gnatcoll-zlib
Summary:        The GNAT Components Collection – ZLib binding
Summary(sv):    GNAT Components Collection – Zlibbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-zlib
This is the ZLib component of the GNAT Components Collection. It is an
interface to ZLib, a library for lossless data compression.

%description -n gnatcoll-zlib -l sv
Detta är ZLib-komponenten i GNAT Components Collection. Den är en gränssnitt
mot biblioteket ZLib för förlustfri datakomprimering.


%package -n gnatcoll-zlib-devel
Summary:        Development files for the GNAT Components Collection – ZLib binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Zlibbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-zlib%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description -n gnatcoll-zlib-devel
This package contains source code and linking information for developing
applications that use the ZLib component of the GNAT Components Collection.
It is an interface to ZLib, a library for lossless data compression.

%description -n gnatcoll-zlib-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder ZLib-komponenten i GNAT Components Collection.
Den är en gränssnitt mot biblioteket ZLib för förlustfri datakomprimering.


%global set_env export GNATCOLL_VERSION=%{version} \
                export BUILD=PROD \
                export LIBRARY_TYPE=relocatable \
                export GNATCOLL_ICONV_OPT=@/dev/null \
                export GNATCOLL_PYTHON_CFLAGS=`python3-config --cflags` \
                export GNATCOLL_PYTHON_LIBS=`python3-config --ldflags`
# Iconv is not a separate library, but an empty GNATCOLL_ICONV_OPT doesn't
# prevent GPRbuild from using the default "-liconv", so it's set to a value
# that makes no difference.


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Convert line breaks.
dos2unix --keepdate gmp/examples/gmp_examples.gpr


###########
## Build ##
###########

%build
%set_env

for component in cpp gmp iconv lzma omp syslog zlib ; do
    gprbuild %{GPRbuild_flags} -P ${component}/gnatcoll_${component}.gpr
done

# Build the binding for Python 3 separately because of the subdir name.
gprbuild %{GPRbuild_flags} -P python3/gnatcoll_python.gpr

# Build the binding for Readline separately because of a necessary
# trampoline and, as a result, executable stack.
gprbuild %{GPRbuild_flags} \
         -largs -Wl,--no-warn-execstack -gargs \
         -P readline/gnatcoll_readline.gpr


#############
## Install ##
#############

%install
%set_env

# Install each component.
for component in cpp gmp iconv lzma omp readline syslog zlib ; do
    %{GPRinstall -s gnatcoll-${component} -a gnatcoll-${component}} \
                 --no-build-var -P ${component}/gnatcoll_${component}.gpr
done

# The binding for Python 3 needs special treatment as its dirname in the source
# tree ("python3") is not reflected in its GNAT project file
# ("gnatcoll_python.gpr").
%{GPRinstall -s gnatcoll-python -a gnatcoll-python} \
             --no-build-var -P python3/gnatcoll_python.gpr

# Fix up the symlinks.
for component in cpp gmp iconv lzma omp python3 readline syslog zlib ; do
    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       %{buildroot}%{_libdir}/libgnatcoll_${component}.so
done

# These files may be of some value to developers:
for component in gmp iconv omp python3 readline syslog ; do
    mkdir --parents %{buildroot}%{_docdir}/gnatcoll-${component}
    cp --preserve=timestamps ${component}/README* \
       --target-directory=%{buildroot}%{_docdir}/gnatcoll-${component}/
done

# Move the examples to the correct location and remove the remaining empty directories.
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/gnatcoll/gmp \
   %{buildroot}%{_docdir}/gnatcoll-gmp/examples

rmdir %{buildroot}%{_datadir}/examples/gnatcoll
rmdir %{buildroot}%{_datadir}/examples

# Install the license with a single pathname that is shared by the subpackages.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 COPYING.RUNTIME \
   --target-directory=%{buildroot}%{_licensedir}/%{name}

# Make the generated usage project files architecture-independent.
for component in cpp gmp iconv lzma omp python readline syslog zlib ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=/python_(cflags|libs)/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Delete the package Linker, which contains linker parameters that a
    #    shared library normally doesn't need, and can contain architecture-
    #    specific pathnames.
    # 4: Delete two unused variables with architecture-specific values from
    #    gnatcoll_python.gpr.
    # 5: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 6: Replace the value of Library_Dir with Directories.Libdir.
    # 7: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done


###########
## Files ##
###########

%files devel
# Empty metapackage.

%files -n gnatcoll-cpp
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING3
%{_libdir}/libgnatcoll_cpp.so.%{version}

%files -n gnatcoll-cpp-devel
%{_GNAT_project_dir}/gnatcoll_cpp.gpr
%dir %{_includedir}/gnatcoll-cpp
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-cpp/cpp_string_support.cpp
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-cpp/*.ad[sb]
%dir %{_libdir}/gnatcoll-cpp
%attr(444,-,-) %{_libdir}/gnatcoll-cpp/*.ali
%{_libdir}/libgnatcoll_cpp.so

%files -n gnatcoll-gmp
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING3
%{_libdir}/libgnatcoll_gmp.so.%{version}

%files -n gnatcoll-gmp-devel
%{_GNAT_project_dir}/gnatcoll_gmp.gpr
%dir %{_includedir}/gnatcoll-gmp
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-gmp/*.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-gmp/*.ad[sb]
%dir %{_libdir}/gnatcoll-gmp
%attr(444,-,-) %{_libdir}/gnatcoll-gmp/*.ali
%{_libdir}/libgnatcoll_gmp.so
# Examples and README:
%{_docdir}/gnatcoll-gmp


%files -n gnatcoll-iconv
%license %{_licensedir}/%{name}
%{_libdir}/libgnatcoll_iconv.so.%{version}

%files -n gnatcoll-iconv-devel
%{_GNAT_project_dir}/gnatcoll_iconv.gpr
%dir %{_includedir}/gnatcoll-iconv
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-iconv/iconv_support.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-iconv/*.ad[sb]
%dir %{_libdir}/gnatcoll-iconv
%attr(444,-,-) %{_libdir}/gnatcoll-iconv/*.ali
%{_libdir}/libgnatcoll_iconv.so
# README:
%{_docdir}/gnatcoll-iconv


%files -n gnatcoll-lzma
%license %{_licensedir}/%{name}
%{_libdir}/libgnatcoll_lzma.so.%{version}

%files -n gnatcoll-lzma-devel
%{_GNAT_project_dir}/gnatcoll_lzma.gpr
%{_includedir}/gnatcoll-lzma
%dir %{_libdir}/gnatcoll-lzma
%attr(444,-,-) %{_libdir}/gnatcoll-lzma/*.ali
%{_libdir}/libgnatcoll_lzma.so


%files -n gnatcoll-omp
%license %{_licensedir}/%{name}
%{_libdir}/libgnatcoll_omp.so.%{version}

%files -n gnatcoll-omp-devel
%{_GNAT_project_dir}/gnatcoll_omp.gpr
%dir %{_includedir}/gnatcoll-omp
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-omp/sort_omp.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-omp/*.ad[sb]
%dir %{_libdir}/gnatcoll-omp
%attr(444,-,-) %{_libdir}/gnatcoll-omp/*.ali
%{_libdir}/libgnatcoll_omp.so
# README:
%{_docdir}/gnatcoll-omp


%files -n gnatcoll-python3
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING3
%{_libdir}/libgnatcoll_python3.so.%{version}

%files -n gnatcoll-python3-devel
%{_GNAT_project_dir}/gnatcoll_python.gpr
%dir %{_includedir}/gnatcoll-python
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-python/python_support.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-python/*.ad[sb]
%dir %{_libdir}/gnatcoll-python
%attr(444,-,-) %{_libdir}/gnatcoll-python/*.ali
%{_libdir}/libgnatcoll_python3.so
# README:
%{_docdir}/gnatcoll-python3


%files -n gnatcoll-readline
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/COPYING3
%{_libdir}/libgnatcoll_readline.so.%{version}

%files -n gnatcoll-readline-devel
%{_GNAT_project_dir}/gnatcoll_readline.gpr
%{_includedir}/gnatcoll-readline
%dir %{_libdir}/gnatcoll-readline
%attr(444,-,-) %{_libdir}/gnatcoll-readline/*.ali
%{_libdir}/libgnatcoll_readline.so
# README:
%{_docdir}/gnatcoll-readline


%files -n gnatcoll-syslog
%license %{_licensedir}/%{name}
%{_libdir}/libgnatcoll_syslog.so.%{version}

%files -n gnatcoll-syslog-devel
%{_GNAT_project_dir}/gnatcoll_syslog.gpr
%dir %{_includedir}/gnatcoll-syslog
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/gnatcoll-syslog/syslog_support.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gnatcoll-syslog/*.ad[sb]
%dir %{_libdir}/gnatcoll-syslog
%attr(444,-,-) %{_libdir}/gnatcoll-syslog/*.ali
%{_libdir}/libgnatcoll_syslog.so
# README:
%{_docdir}/gnatcoll-syslog


%files -n gnatcoll-zlib
%license %{_licensedir}/%{name}
%{_libdir}/libgnatcoll_zlib.so.%{version}

%files -n gnatcoll-zlib-devel
%{_GNAT_project_dir}/gnatcoll_zlib.gpr
%{_includedir}/gnatcoll-zlib
%dir %{_libdir}/gnatcoll-zlib
%attr(444,-,-) %{_libdir}/gnatcoll-zlib/*.ali
%{_libdir}/libgnatcoll_zlib.so


###############
## Changelog ##
###############

%changelog
* Wed Jan 15 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.0.0-2
- Rebuilt with GCC 15 prerelease.

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.
- New subpackage for bindings to the C++ ISO/IEC 14882:1998(E) string class.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-2
- Development package dependencies have been adjusted.

* Sun May 05 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- Permit the Readline binding to have an executable stack.

* Sun May 05 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0.
- Removed backport patch gnatcoll-bindings-transition-from-pyton-37-to-39.patch.

* Sat May 04 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0.
- License fields now contain SPDX license expressions.
- Added a license to the package that contains the Python bindings.
- Enabled the Python 3 binding.
- Improved spec file readability.
- Added the LZMA binding.
- Added the OpenMP (sorting) component.
- Added the ZLib binding.

* Sun Feb 11 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-17
- Rebuilt with XMLada 24 and LibGPR 24.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-14
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-12
- Rebuilt with XMLada 23 and LibGPR 23.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-10
- Rebuilt with GCC 13.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-6
- Updated the licenses.

* Mon Feb 08 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-5
- Adjusted the usage project files.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-3
- Specified epoch of dependencies.

* Mon Jan 11 2021 Pavel Zhukov <pzhukov@redhat.com> - 2:21.0.0-2
- Specify fedora-gnat-projects-common version
- Remove obsolete comments

* Mon Jan 11 2021 Pavel Zhukov <pzhukov@redhat.com> - 2:21.0.0-1
- New version 21.0.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-3
- Tagged the license file as such.

* Fri Mar 29 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-2
- Added more macro usage, more comments and ownership of a directory.

* Sat Mar 16 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-1
- new package
