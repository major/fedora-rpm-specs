%global packname rmarkdown
%global packver  2.24
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((dygraphs)\\)

# Recursive dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Dynamic Documents for R

# Main is GPLv3; see bundled Provides below for others.
License:          GPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT AND W3C
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Remove-unused-minified-ioslides-files.patch
Patch0004:        0004-Add-original-non-minified-Bootswatch-themes.patch
Patch0006:        0006-Add-source-for-code-prettify.patch
Patch0007:        0007-Skip-shiny-tests.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-bslib >- 0.2.51, R-evaluate >= 0.13, R-fontawesome >= 0.5.0, R-htmltools >= 0.5.1, R-jquerylib, R-jsonlite, R-knitr >= 1.22, R-methods, R-stringr >= 1.2.0, R-tinytex >= 0.31, R-tools, R-utils, R-xfun >= 0.36, R-yaml >= 2.1.19
# Suggests:  R-shiny >= 1.6.0, R-tufte, R-testthat >= 3.0.3, R-digest, R-dygraphs, R-vctrs, R-tibble, R-fs, R-rsconnect, R-withr >= 2.4.2, R-sass >= 0.4.0, R-downlit >= 0.4.0, R-katex >= 1.4.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         pandoc >= 1.14

BuildRequires:    git-core
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pandoc >= 1.14
BuildRequires:    golang-github-tdewolff-minify
BuildRequires:    R-bslib >= 0.2.5.1
BuildRequires:    R-evaluate >= 0.13
BuildRequires:    R-fontawesome >= 0.5.0
BuildRequires:    R-htmltools >= 0.5.1
BuildRequires:    R-jquerylib
BuildRequires:    R-jsonlite
BuildRequires:    R-knitr >= 1.22
BuildRequires:    R-methods
BuildRequires:    R-stringr >= 1.2.0
BuildRequires:    R-tinytex >= 0.31
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-xfun >= 0.36
BuildRequires:    R-yaml >= 2.1.19
%if %{with_suggests}
BuildRequires:    R-digest
BuildRequires:    R-dygraphs
BuildRequires:    R-fs
BuildRequires:    R-rsconnect
BuildRequires:    R-downlit >= 0.4.0
BuildRequires:    R-katex >= 1.4.0
BuildRequires:    R-sass >= 0.4.0
BuildRequires:    R-shiny >= 1.6.0
BuildRequires:    R-testthat >= 3.0.3
BuildRequires:    R-tibble
BuildRequires:    R-tufte
BuildRequires:    R-vctrs
BuildRequires:    R-withr >= 2.4.2
%endif

# These are not all packaged, but should *probably* be the names if they are.

# MIT; inst/rmd/h/bootstrap/
# https://github.com/twbs/bootstrap/releases/tag/v3.3.5
Provides:         bundled(xstatic-bootstrap-common) = 3.3.5
BuildRequires:    adobe-source-sans-pro-fonts
Requires:         adobe-source-sans-pro-fonts
BuildRequires:    glyphicons-halflings-fonts
Requires:         glyphicons-halflings-fonts
BuildRequires:    glyphography-newscycle-fonts
Requires:         glyphography-newscycle-fonts
BuildRequires:    google-roboto-fonts
Requires:         google-roboto-fonts
BuildRequires:    impallari-raleway-fonts
Requires:         impallari-raleway-fonts
BuildRequires:    lato-fonts
Requires:         lato-fonts

# BSD; inst/rmd/h/highlightjs/ (unbundled)
#BuildRequires:    js-highlight
#Requires:         js-highlight
# Currently broken in Fedora
Provides:         bundled(js-highlight) = 9.12.0

# MIT; inst/rmd/h/ionicons/
# http://ionicons.com/
Provides:         bundled(ionicons-fonts) = 2.0.1

# MIT; inst/rmd/h/jquery/
Provides:         bundled(js-jquery1) = 1.12.4

# MIT; inst/rmd/h/jqueryui (outdated in Fedora)
Provides:         bundled(xstatic-jquery-ui-common) = 1.11.4

# MIT; inst/rmd/h/navigation-1.1/tabsets.js
# https://github.com/aidanlister/jquery-stickytabs (partially)
Provides:         bundled(js-jquery-stickytabs) = 1.2.4

# MIT; inst/rmd/h/tocify/
# http://gregfranko.com/jquery.tocify.js/
Provides:         bundled(js-jquery-tocify) = 1.9.1

# ASL 2.0; inst/rmd/ioslides/ioslides-13.5.1/
Provides:         bundled(js-ioslides) = 13.5.1
# MIT; inst/rmd/ioslides/ioslides-13.5.1/js/hammer.js
# https://hammerjs.github.io/
Provides:         bundled(js-hammer) = 0.4
# MIT & BSD; inst/rmd/ioslides/ioslides-13.5.1/js/modernizr.custom.45394.js
# https://modernizr.com/
Provides:         bundled(js-modernizr) = 2.5.3
# ASL 2.0; inst/rmd/ioslides/ioslides-13.5.1/js/prettify/
# https://github.com/google/code-prettify
Provides:         bundled(js-code-prettify) = 20130304
BuildRequires:    open-sans-fonts
Requires:         open-sans-fonts
BuildRequires:    adobe-source-code-pro-fonts
Requires:         adobe-source-code-pro-fonts

# W3C; inst/rmd/slidy/Slidy2/
# https://www.w3.org/Talks/Tools/Slidy2/
Provides:         bundled(js-slidy) = 2

%description
Convert R Markdown documents into a variety of formats.


%prep
%setup -q -c -n %{packname}
%autosetup -D -T -n %{packname}/%{packname} -S git

# Must be removed: https://bugzilla.redhat.com/show_bug.cgi?id=961642#c4
rm inst/rmd/h/bootstrap/css/fonts/Ubuntu.ttf

# Fix executable bits
chmod -x inst/rmd/h/ionicons/{LICENSE,css/*.css,fonts/*.ttf}
chmod -x inst/rmd/ioslides/ioslides-13.5.1/js/hammer.js

# This does nothing but reset the -n path.
%setup -q -D -T -n %{packname}


%build
gominify --type css \
    < %{packname}/inst/rmd/h/ionicons/css/ionicons.css \
    > %{packname}/inst/rmd/h/ionicons/css/ionicons.min.css
pushd %{packname}/inst/rmd/h/bootstrap/css/
for file in bootstrap bootstrap-theme cerulean cosmo darkly flatly journal lumen paper readable sandstone simplex spacelab united yeti; do
    gominify --type css < ${file}.css > ${file}.min.css
done
popd


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}
    # Remove bundled fonts in ioslides.
    pushd rmd/ioslides/ioslides-13.5.1/fonts
        ln -sf /usr/share/fonts/open-sans/OpenSans-Regular.ttf OpenSans.ttf
        for f in Italic SemiboldItalic Semibold; do
            ln -sf /usr/share/fonts/open-sans/OpenSans-${f}.ttf OpenSans${f}.ttf
        done
        rm -f SourceCodePro*.ttf
        ln -sf /usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf SourceCodePro.otf
        sed -i "s/SourceCodePro.ttf) format('true/SourceCodePro.otf) format('open/" fonts.css
    popd
    # Remove bundled fonts from bootstrap.
    pushd rmd/h/bootstrap/css/fonts
        %if 0%{?fedora} > 38
        ln -sf /usr/share/fonts/lato-fonts/Lato-Regular.ttf Lato.ttf
        ln -sf /usr/share/fonts/lato-fonts/Lato-Bold.ttf LatoBold.ttf
        ln -sf /usr/share/fonts/lato-fonts/Lato-Italic.ttf LatoItalic.ttf
        %else
        ln -sf /usr/share/fonts/lato/Lato-Regular.ttf Lato.ttf
        ln -sf /usr/share/fonts/lato/Lato-Bold.ttf LatoBold.ttf
        ln -sf /usr/share/fonts/lato/Lato-Italic.ttf LatoItalic.ttf
        %endif
        ln -sf /usr/share/fonts/glyphography-newscycle-fonts/newscycle-regular.ttf NewsCycle.ttf
        ln -sf /usr/share/fonts/glyphography-newscycle-fonts/newscycle-bold.ttf NewsCycleBold.ttf
        ln -sf /usr/share/fonts/open-sans/OpenSans-Regular.ttf OpenSans.ttf
        for f in Bold BoldItalic Italic Light LightItalic; do
            ln -sf /usr/share/fonts/open-sans/OpenSans-${f}.ttf OpenSans${f}.ttf
        done
        ln -sf /usr/share/fonts/impallari-raleway-fonts/Raleway-Regular.ttf Raleway.ttf
        for f in Bold; do
            ln -sf /usr/share/fonts/impallari-raleway-fonts/Raleway-${f}.ttf Raleway${f}.ttf
        done
        ln -sf /usr/share/fonts/google-roboto/Roboto-Regular.ttf Roboto.ttf
        for f in Light Medium Bold; do
            ln -sf /usr/share/fonts/google-roboto/Roboto-${f}.ttf Roboto${f}.ttf
        done
        rm -f SourceSansPro*.ttf
        ln -sf /usr/share/fonts/adobe-source-sans-pro-fonts/SourceSans3-Regular.otf SourceSansPro.otf
        ln -sf /usr/share/fonts/adobe-source-sans-pro-fonts/SourceSans3-It.otf SourceSansProItalic.otf
        for f in Bold Light; do
            ln -sf /usr/share/fonts/adobe-source-sans-pro-fonts/SourceSans3-${f}.otf SourceSansPro${f}.otf
        done
        sed -i ../{cosmo,lumen}.min.css \
            -e "s/SourceSansPro.ttf) format('true/SourceSansPro.otf) format('open/" \
            -e "s/SourceSansProLight.ttf) format('true/SourceSansProLight.otf) format('open/" \
            -e "s/SourceSansProBold.ttf) format('true/SourceSansProBold.otf) format('open/" \
            -e "s/SourceSansProItalic.ttf) format('true/SourceSansProItalic.otf) format('open/"
    popd
    pushd rmd/h/bootstrap/fonts
        rm -f glyphicons-halflings*
        ln -sf /usr/share/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf glyphicons-halflings-regular.ttf
    popd
popd


%check
%if %{with_suggests}
%{_bindir}/R CMD check --ignore-vignettes --no-manual %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes --no-manual --no-tests %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/rmarkdown
%dir %{rlibdir}/%{packname}/rmd
%{rlibdir}/%{packname}/rmd/fragment
%dir %{rlibdir}/%{packname}/rmd/h
%{rlibdir}/%{packname}/rmd/h/_navbar.html
%{rlibdir}/%{packname}/rmd/h/accessibility
%{rlibdir}/%{packname}/rmd/h/anchor-sections
%{rlibdir}/%{packname}/rmd/h/default.html
%{rlibdir}/%{packname}/rmd/h/bootstrap
%{rlibdir}/%{packname}/rmd/h/highlightjs
%{rlibdir}/%{packname}/rmd/h/ionicons
%{rlibdir}/%{packname}/rmd/h/jqueryui
# %%{rlibdir}/%%{packname}/rmd/h/jqueryui-AUTHORS.txt
%{rlibdir}/%{packname}/rmd/h/navigation-1.1
%{rlibdir}/%{packname}/rmd/h/pagedtable-1.1
%{rlibdir}/%{packname}/rmd/h/pandoc
%{rlibdir}/%{packname}/rmd/h/rmarkdown
%{rlibdir}/%{packname}/rmd/h/rsiframe-1.1
%{rlibdir}/%{packname}/rmd/h/shiny-header.html
%{rlibdir}/%{packname}/rmd/h/tabset/
%{rlibdir}/%{packname}/rmd/h/tocify
%{rlibdir}/%{packname}/rmd/ioslides
%{rlibdir}/%{packname}/rmd/latex
%{rlibdir}/%{packname}/rmd/site
%{rlibdir}/%{packname}/rmd/slidy
%{rlibdir}/%{packname}/rstudio


%changelog
%autochangelog
