Name:           R-viridisLite
Version:        %R_rpm_version 0.4.2
Release:        %autorelease
Summary:        Colorblind-Friendly Color Maps (Lite Version)

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Color maps designed to improve graph readability for readers with common
forms of color blindness and/or color vision deficiency. The color maps are
also perceptually-uniform, both in regular form and also when converted to
black-and-white for printing. This is the 'lite' version of the 'viridis'
package that also contains 'ggplot2' bindings for discrete and continuous
color and fill scales and can be found at
<https://cran.r-project.org/package=viridis>.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
