Name:           R-colorspace
Version:        %R_rpm_version 2.1-2
Release:        %autorelease
Summary:        A Toolbox for Manipulating and Assessing Colors and Palettes

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB, and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided along
with corresponding ggplot2 color scales. Color palette choice is aided by an
interactive app (with either a Tcl/Tk or a shiny graphical user interface) and
shiny apps with an HCL color picker and a color vision deficiency emulator.
Plotting functions for displaying and assessing palettes include color
swatches, visualizations of the HCL space, and trajectories in HCL and/or RGB
spectrum. Color manipulation functions include: desaturation,
lightening/darkening, mixing, and simulation of color vision deficiencies
(deutanomaly, protanomaly, tritanomaly). Details can be found on the project
web page at <http://colorspace.R-Forge.R-project.org/> and in the accompanying
scientific paper: Zeileis et al. (2020, Journal of Statistical Software,
<doi:10.18637/jss.v096.i01>).

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
