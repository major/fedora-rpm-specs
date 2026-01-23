Name:           R-rJava
Version:        %R_rpm_version 1.0-14
Release:        %autorelease
Summary:        Low-Level R to Java Interface

License:        LGPL-2.1-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-javadoc < %{version}-%{release}
ExclusiveArch:  %{java_arches}

%description
Low-level interface to Java VM very much like .C/.Call and friends.
Allows creation of objects, calling methods and accessing fields.

%prep
%autosetup -c
rm rJava/inst/jri/*.jar

%generate_buildrequires
%R_buildrequires

%build
# rebuild jars
find rJava/jri/REngine -name Makefile -exec sed -i 's/1.6/1.8/g' {} \;
%make_build -C rJava/jri/REngine
%make_build -C rJava/jri/REngine/JRI
mv rJava/jri/REngine/{REngine,JRI/JRIEngine}.jar rJava/inst/jri/

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
