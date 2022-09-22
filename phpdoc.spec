#
# Fedora spec file for phpdoc
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      phpDocumentor2
%global github_version   2.9.1
%global github_commit    2e4f981a55ebe6f5db592d7da892d13d5b3c7816

%global composer_vendor  phpdocumentor
%global composer_project phpdocumentor

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "cilex/cilex": "~1.0"
%global cilex_min_ver 1.0
%global cilex_max_ver 2.0
# "erusev/parsedown": "~1.0"
%global erusev_parsedown_min_ver 1.0
%global erusev_parsedown_max_ver 2.0
# "jms/serializer": ">=0.12"
#     NOTE: Max version added
%global jms_serializer_min_ver 0.12
%global jms_serializer_max_ver 2.0
# "mikey179/vfsStream": "~1.2"
%global mikey179_vfsstream_min_ver 1.2
%global mikey179_vfsstream_max_ver 2.0
# "mockery/mockery": "~0.9@dev"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0
# "monolog/monolog": "~1.6"
%global monolog_min_ver 1.6
%global monolog_max_ver 2.0
# "phpdocumentor/fileset": "~1.0"
%global phpdocumentor_fileset_min_ver 1.0
%global phpdocumentor_fileset_max_ver 2.0
# "phpdocumentor/graphviz": "~1.0"
%global phpdocumentor_graphviz_min_ver 1.0
%global phpdocumentor_graphviz_max_ver 2.0
# "phpdocumentor/reflection": "^3.0"
%global phpdocumentor_reflection_min_ver 3.0
%global phpdocumentor_reflection_max_ver 4.0
# "phpdocumentor/reflection-docblock": "~2.0"
%global phpdocumentor_reflection_docblock_min_ver 2.0
%global phpdocumentor_reflection_docblock_max_ver 3.0
# "symfony/config": "~2.3"
# "symfony/console": "~2.3"
# "symfony/event-dispatcher": "~2.1"
# "symfony/expression-language": "~2.4"
# "symfony/process": "~2.0"
# "symfony/stopwatch": "~2.3"
# "symfony/validator": "~2.2"
#     NOTE: Min version not 2.4 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 3.0
# "twig/twig": "~1.3"
%global twig_min_ver 1.3
%global twig_max_ver 2.0
# "zendframework/zend-cache": "~2.1"
%global zendframework_cache_min_ver 2.1
%global zendframework_cache_max_ver 3.0
# "zendframework/zend-config": "~2.1"
%global zendframework_config_min_ver 2.1
%global zendframework_config_max_ver 3.0
# "zendframework/zend-filter": "~2.1"
%global zendframework_filter_min_ver 2.1
%global zendframework_filter_max_ver 3.0
# "zendframework/zend-i18n": "~2.1"
%global zendframework_i18n_min_ver 2.1
%global zendframework_i18n_max_ver 3.0
# "zendframework/zend-serializer": "~2.1"
%global zendframework_serializer_min_ver 2.1
%global zendframework_serializer_max_ver 3.0
# "zendframework/zend-servicemanager": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_servicemanager_min_ver 2.1
%global zendframework_servicemanager_max_ver 4.0
# "zendframework/zend-stdlib": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_stdlib_min_ver 2.1
%global zendframework_stdlib_max_ver 4.0
# "zetacomponents/document": ">=1.3.1"
#     NOTE: Max version to restrict to one major version
%global zetacomponents_document_min_ver 1.3.1
%global zetacomponents_document_max_ver 2.0
# "webmozart/assert": "^1.2",
%global webmozart_assert_min_ver 1.2
%global webmozart_assert_max_ver 2

# Build using "--with tests" to enable tests
%bcond_with tests

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          phpdoc
Version:       %{github_version}
Release:       7%{?github_release}%{?dist}
Summary:       Documentation generator for PHP

# License breakdown:
# * MIT
#     * phpdoc
#     * data/templates/abstract/css/sen.full.min.css
#     * data/templates/clean/css/font-awesome.min.css
#     * data/templates/clean/css/prism.css
#     * data/templates/clean/js/jquery-1.11.0.min.js
#     * data/templates/clean/js/jquery.mousewheel.js
#     * data/templates/clean/js/prism.min.js
#     * data/templates/clean/js/ui/1.10.4/jquery-ui.min.js
#     * data/templates/responsive/img/iviewer/*
#     * data/templates/responsive/js/jquery.mousewheel.min.js
#     * data/templates/responsive/js/jquery.xml2json.js
# * ASL 2.0
#     * data/templates/clean/css/bootstrap-combined.no-icons.min.css
#     * data/templates/clean/js/bootstrap.min.js
#     * data/templates/responsive/css/bootstrap-responsive.css
#     * data/templates/responsive/css/bootstrap-responsive.min.css
#     * data/templates/responsive/css/bootstrap.css
#     * data/templates/responsive/css/bootstrap.min.css
#     * data/templates/responsive/js/bootstrap.js
#     * data/templates/responsive/js/bootstrap.min.js
#     * data/templates/responsive/js/prettify/*
#     * data/templates/responsive/js/prettify/lang-clj.js
#     * docs/.static/css/bootstrap-responsive.css
#     * docs/.static/css/bootstrap.min.css
#     * docs/.static/css/prettify.css
#     * docs/.static/js/bootstrap.js
#     * docs/.static/js/prettify/prettify.min.js
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap-responsive.css
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap-responsive.min.css
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap.css
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap.min.css
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/prettify.css
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/bootstrap.min.js
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/prettify/*
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/prettify/lang-clj.js
# * BSD
#     * data/templates/old-ocean/js/SVGPan.js
#     * data/templates/responsive/js/SVGPan.js
#     * docs/.exts/__init__.py
#     * docs/.exts/plantuml.py
#     * docs/.exts/plantuml.pyc
#     * docs/.static/default.css
# * CC-BY
#     * data/templates/responsive/img/glyphicons-halflings-white.png
#     * data/templates/responsive/img/glyphicons-halflings.png
#     * docs/.static/img/glyphicons-halflings-white.png
#     * docs/.static/img/glyphicons-halflings.png
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/img/glyphicons-halflings-white.png
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/img/glyphicons-halflings.png
# * DWPL and MIT
#     * data/templates/abstract/js/jquery.tools.min.js
#     * data/templates/old-ocean/js/jquery.tools.min.js
#     * data/templates/responsive/js/jquery.tools.min.js
# * MIT and GPLv2
#     * data/templates/clean/js/html5.js
# * MIT and GPLv2 and Public Domain and CC-BY
#     * data/templates/responsive/js/jqplot/*
# * MIT and GPLv3
#     * data/templates/abstract/js/jquery-ui-1.8.2.custom.min.js
#     * data/templates/abstract/js/jquery.cookie.js
#     * data/templates/abstract/js/jquery.panzoom.js
#     * data/templates/abstract/js/jquery.treeview.js
#     * data/templates/clean/js/jquery.dotdotdot-1.5.9.js
#     * data/templates/clean/js/jquery.dotdotdot-1.5.9.min.js
#     * data/templates/clean/js/jquery.iviewer.js
#     * data/templates/clean/js/jquery.iviewer.min.js
#     * data/templates/old-ocean/css/black-tie/jquery-ui-1.8.2.custom.css
#     * data/templates/old-ocean/js/jquery-ui-1.8.2.custom.min.js
#     * data/templates/old-ocean/js/jquery.cookie.js
#     * data/templates/old-ocean/js/jquery.panzoom.js
#     * data/templates/old-ocean/js/jquery.splitter.js
#     * data/templates/old-ocean/js/jquery.treeview.js
#     * data/templates/responsive/js/jquery-ui-1.8.2.custom.min.js
#     * data/templates/responsive/js/jquery.cookie.js
#     * data/templates/responsive/js/jquery.iviewer.js
#     * data/templates/responsive/js/jquery.iviewer.min.js
#     * data/templates/responsive/js/jquery.panzoom.js
#     * data/templates/responsive/js/jquery.splitter.js
#     * data/templates/responsive/js/jquery.treeview.js
#     * data/templates/zend/css/black-tie/jquery-ui-1.8.2.custom.css
#     * data/templates/zend/js/jquery.splitter.js
#     * docs/.static/js/jquery-ui-1.8.2.custom.min.js
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/jquery-ui-1.8.2.custom.min.js
# * MIT or GPLv2
#     * data/templates/abstract/js/jquery-1.4.2.min.js
#     * data/templates/new-black/css/jquery-ui.css
#     * data/templates/new-black/css/phpdoc/jquery-ui-1.8.16.custom.css
#     * data/templates/old-ocean/js/jquery-1.4.2.min.js
#     * data/templates/old-ocean/js/jquery-1.7.1.min.js
#     * data/templates/responsive/js/jquery-1.4.2.min.js
#     * data/templates/responsive/js/jquery-1.7.1.min.js
#     * docs/.static/js/jquery-1.7.1.min.js
#     * src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/jquery-1.7.1.min.js
# * OFL
#     * data/templates/clean/font/fontawesome-webfont.eot
#     * data/templates/clean/font/fontawesome-webfont.svg
#     * data/templates/clean/font/fontawesome-webfont.ttf
#     * data/templates/clean/font/fontawesome-webfont.woff
#     * data/templates/clean/font/FontAwesome.otf
License:       MIT and ASL 2.0 and BSD and CC-BY and (DWPL and MIT) and (MIT and GPLv2) and (MIT and GPLv2 and Public Domain and CC-BY) and (MIT and GPLv3) and (MIT or GPLv2) and OFL
URL:           https://www.phpdoc.org/

# GitHub export does not include tests.
# Run phpdoc-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Adjust vendor dir
Patch0:        %{name}-adjust-vendor-dir.patch
# Adjust templates dir
Patch1:        %{name}-adjust-templates-dir.patch

BuildArch:     noarch
# Composer autoloader generation
BuildRequires: composer
# Tests
BuildRequires: php-cli
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(cilex/cilex) < %{cilex_max_ver} with php-composer(cilex/cilex) >= %{cilex_min_ver})
BuildRequires: (php-composer(erusev/parsedown) < %{erusev_parsedown_max_ver} with php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver})
BuildRequires: (php-composer(jms/serializer) < %{jms_serializer_max_ver} with php-composer(jms/serializer) >= %{jms_serializer_min_ver})
BuildRequires: (php-composer(mikey179/vfsStream) < %{mikey179_vfsstream_max_ver} with php-composer(mikey179/vfsStream) >= %{mikey179_vfsstream_min_ver})
BuildRequires: (php-composer(mockery/mockery) < %{mockery_max_ver} with php-composer(mockery/mockery) >= %{mockery_min_ver})
BuildRequires: (php-composer(monolog/monolog) < %{monolog_max_ver} with php-composer(monolog/monolog) >= %{monolog_min_ver})
BuildRequires: (php-composer(phpdocumentor/fileset) < %{phpdocumentor_fileset_max_ver} with php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver})
BuildRequires: (php-composer(phpdocumentor/graphviz) < %{phpdocumentor_graphviz_max_ver} with php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver})
BuildRequires: (php-composer(phpdocumentor/reflection-docblock) < %{phpdocumentor_reflection_docblock_max_ver} with php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver})
BuildRequires: (php-composer(phpdocumentor/reflection) < %{phpdocumentor_reflection_max_ver} with php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver})
BuildRequires: (php-composer(symfony/config) < %{symfony_max_ver} with php-composer(symfony/config) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/console) < %{symfony_max_ver} with php-composer(symfony/console) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/event-dispatcher) < %{symfony_max_ver} with php-composer(symfony/event-dispatcher) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/expression-language) < %{symfony_max_ver} with php-composer(symfony/expression-language) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/process) < %{symfony_max_ver} with php-composer(symfony/process) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/stopwatch) < %{symfony_max_ver} with php-composer(symfony/stopwatch) >= %{symfony_min_ver})
BuildRequires: (php-composer(symfony/validator) < %{symfony_max_ver} with php-composer(symfony/validator) >= %{symfony_min_ver})
BuildRequires: (php-composer(twig/twig) < %{twig_max_ver} with php-composer(twig/twig) >= %{twig_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-cache) < %{zendframework_cache_max_ver} with php-autoloader(zendframework/zend-cache) >= %{zendframework_cache_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-config) < %{zendframework_config_max_ver} with php-autoloader(zendframework/zend-config) >= %{zendframework_config_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-filter) < %{zendframework_filter_max_ver} with php-autoloader(zendframework/zend-filter) >= %{zendframework_filter_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-i18n) < %{zendframework_i18n_max_ver} with php-autoloader(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-serializer) < %{zendframework_serializer_max_ver} with php-autoloader(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-servicemanager) < %{zendframework_servicemanager_max_ver} with php-autoloader(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver})
BuildRequires: (php-autoloader(zendframework/zend-stdlib) < %{zendframework_stdlib_max_ver} with php-autoloader(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver})
BuildRequires: (php-composer(zetacomponents/document) < %{zetacomponents_document_max_ver} with php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver})
BuildRequires: (php-composer(webmozart/assert) < %{webmozart_assert_max_ver} with php-composer(webmozart/assert) >= %{webmozart_assert_min_ver})
%else
BuildRequires: php-composer(cilex/cilex) <  %{cilex_max_ver}
BuildRequires: php-composer(cilex/cilex) >= %{cilex_min_ver}
BuildRequires: php-composer(erusev/parsedown) <  %{erusev_parsedown_max_ver}
BuildRequires: php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver}
BuildRequires: php-composer(jms/serializer) <  %{jms_serializer_max_ver}
BuildRequires: php-composer(jms/serializer) >= %{jms_serializer_min_ver}
BuildRequires: php-composer(mikey179/vfsStream) <  %{mikey179_vfsstream_max_ver}
BuildRequires: php-composer(mikey179/vfsStream) >= %{mikey179_vfsstream_min_ver}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(monolog/monolog) <  %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
BuildRequires: php-composer(phpdocumentor/fileset) <  %{phpdocumentor_fileset_max_ver}
BuildRequires: php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver}
BuildRequires: php-composer(phpdocumentor/graphviz) <  %{phpdocumentor_graphviz_max_ver}
BuildRequires: php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection-docblock) <  %{phpdocumentor_reflection_docblock_max_ver}
BuildRequires: php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection) <  %{phpdocumentor_reflection_max_ver}
BuildRequires: php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver}
BuildRequires: php-composer(symfony/config) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/config) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/expression-language) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/expression-language) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/stopwatch) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/stopwatch) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/validator) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/validator) >= %{symfony_min_ver}
BuildRequires: php-composer(twig/twig) <  %{twig_max_ver}
BuildRequires: php-composer(twig/twig) >= %{twig_min_ver}
BuildRequires: php-autoloader(zendframework/zend-cache) <  %{zendframework_cache_max_ver}
BuildRequires: php-autoloader(zendframework/zend-cache) >= %{zendframework_cache_min_ver}
BuildRequires: php-autoloader(zendframework/zend-config) <  %{zendframework_config_max_ver}
BuildRequires: php-autoloader(zendframework/zend-config) >= %{zendframework_config_min_ver}
BuildRequires: php-autoloader(zendframework/zend-filter) <  %{zendframework_filter_max_ver}
BuildRequires: php-autoloader(zendframework/zend-filter) >= %{zendframework_filter_min_ver}
BuildRequires: php-autoloader(zendframework/zend-i18n) <  %{zendframework_i18n_max_ver}
BuildRequires: php-autoloader(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver}
BuildRequires: php-autoloader(zendframework/zend-serializer) <  %{zendframework_serializer_max_ver}
BuildRequires: php-autoloader(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver}
BuildRequires: php-autoloader(zendframework/zend-servicemanager) <  %{zendframework_servicemanager_max_ver}
BuildRequires: php-autoloader(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver}
BuildRequires: php-autoloader(zendframework/zend-stdlib) <  %{zendframework_stdlib_max_ver}
BuildRequires: php-autoloader(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver}
BuildRequires: php-composer(zetacomponents/document) <  %{zetacomponents_document_max_ver}
BuildRequires: php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver}
BuildRequires: php-composer(webmozart/assert) < %{webmozart_assert_max_ver}
BuildRequires: php-composer(webmozart/assert) >= %{webmozart_assert_min_ver}
%endif
## phpcompatinfo (computed from version 2.9.1)
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-filter
BuildRequires: php-iconv
BuildRequires: php-igbinary
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xsl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(cilex/cilex) < %{cilex_max_ver} with php-composer(cilex/cilex) >= %{cilex_min_ver})
Requires:      (php-composer(erusev/parsedown) < %{erusev_parsedown_max_ver} with php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver})
Requires:      (php-composer(jms/serializer) < %{jms_serializer_max_ver} with php-composer(jms/serializer) >= %{jms_serializer_min_ver})
Requires:      (php-composer(monolog/monolog) < %{monolog_max_ver} with php-composer(monolog/monolog) >= %{monolog_min_ver})
Requires:      (php-composer(phpdocumentor/fileset) < %{phpdocumentor_fileset_max_ver} with php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver})
Requires:      (php-composer(phpdocumentor/graphviz) < %{phpdocumentor_graphviz_max_ver} with php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver})
Requires:      (php-composer(phpdocumentor/reflection) < %{phpdocumentor_reflection_max_ver} with php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver})
Requires:      (php-composer(phpdocumentor/reflection-docblock) < %{phpdocumentor_reflection_docblock_max_ver} with php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver})
Requires:      (php-composer(symfony/config) < %{symfony_max_ver} with php-composer(symfony/config) >= %{symfony_min_ver})
Requires:      (php-composer(symfony/console) < %{symfony_max_ver} with php-composer(symfony/console) >= %{symfony_min_ver})
Requires:      (php-composer(symfony/event-dispatcher) < %{symfony_max_ver} with php-composer(symfony/event-dispatcher) >= %{symfony_min_ver})
Requires:      (php-composer(symfony/process) < %{symfony_max_ver} with php-composer(symfony/process) >= %{symfony_min_ver})
Requires:      (php-composer(symfony/stopwatch) < %{symfony_max_ver} with php-composer(symfony/stopwatch) >= %{symfony_min_ver})
Requires:      (php-composer(symfony/validator) < %{symfony_max_ver} with php-composer(symfony/validator) >= %{symfony_min_ver})
Requires:      (php-composer(twig/twig) < %{twig_max_ver} with php-composer(twig/twig) >= %{twig_min_ver})
Requires:      (php-autoloader(zendframework/zend-cache) < %{zendframework_cache_max_ver} with php-autoloader(zendframework/zend-cache) >= %{zendframework_cache_min_ver})
Requires:      (php-autoloader(zendframework/zend-config) < %{zendframework_config_max_ver} with php-autoloader(zendframework/zend-config) >= %{zendframework_config_min_ver})
Requires:      (php-autoloader(zendframework/zend-filter) < %{zendframework_filter_max_ver} with php-autoloader(zendframework/zend-filter) >= %{zendframework_filter_min_ver})
Requires:      (php-autoloader(zendframework/zend-i18n) < %{zendframework_i18n_max_ver} with php-autoloader(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver})
Requires:      (php-autoloader(zendframework/zend-serializer) < %{zendframework_serializer_max_ver} with php-autoloader(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver})
Requires:      (php-autoloader(zendframework/zend-servicemanager) < %{zendframework_servicemanager_max_ver} with php-autoloader(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver})
Requires:      (php-autoloader(zendframework/zend-stdlib) < %{zendframework_stdlib_max_ver} with php-autoloader(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver})
Requires:      (php-composer(zetacomponents/document) < %{zetacomponents_document_max_ver} with php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver})
Requires:      (php-composer(webmozart/assert) < %{webmozart_assert_max_ver} with php-composer(webmozart/assert) >= %{webmozart_assert_min_ver})
%else
Requires:      php-composer(cilex/cilex) <  %{cilex_max_ver}
Requires:      php-composer(cilex/cilex) >= %{cilex_min_ver}
Requires:      php-composer(erusev/parsedown) <  %{erusev_parsedown_max_ver}
Requires:      php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver}
Requires:      php-composer(jms/serializer) <  %{jms_serializer_max_ver}
Requires:      php-composer(jms/serializer) >= %{jms_serializer_min_ver}
Requires:      php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires:      php-composer(phpdocumentor/fileset) <  %{phpdocumentor_fileset_max_ver}
Requires:      php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver}
Requires:      php-composer(phpdocumentor/graphviz) <  %{phpdocumentor_graphviz_max_ver}
Requires:      php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver}
Requires:      php-composer(phpdocumentor/reflection) <  %{phpdocumentor_reflection_max_ver}
Requires:      php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) <  %{phpdocumentor_reflection_docblock_max_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver}
Requires:      php-composer(symfony/config) <  %{symfony_max_ver}
Requires:      php-composer(symfony/config) >= %{symfony_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/process) <  %{symfony_max_ver}
Requires:      php-composer(symfony/process) >= %{symfony_min_ver}
Requires:      php-composer(symfony/stopwatch) <  %{symfony_max_ver}
Requires:      php-composer(symfony/stopwatch) >= %{symfony_min_ver}
Requires:      php-composer(symfony/validator) <  %{symfony_max_ver}
Requires:      php-composer(symfony/validator) >= %{symfony_min_ver}
Requires:      php-composer(twig/twig) <  %{twig_max_ver}
Requires:      php-composer(twig/twig) >= %{twig_min_ver}
Requires:      php-autoloader(zendframework/zend-cache) <  %{zendframework_cache_max_ver}
Requires:      php-autoloader(zendframework/zend-cache) >= %{zendframework_cache_min_ver}
Requires:      php-autoloader(zendframework/zend-config) <  %{zendframework_config_max_ver}
Requires:      php-autoloader(zendframework/zend-config) >= %{zendframework_config_min_ver}
Requires:      php-autoloader(zendframework/zend-filter) <  %{zendframework_filter_max_ver}
Requires:      php-autoloader(zendframework/zend-filter) >= %{zendframework_filter_min_ver}
Requires:      php-autoloader(zendframework/zend-i18n) <  %{zendframework_i18n_max_ver}
Requires:      php-autoloader(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver}
Requires:      php-autoloader(zendframework/zend-serializer) <  %{zendframework_serializer_max_ver}
Requires:      php-autoloader(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver}
Requires:      php-autoloader(zendframework/zend-servicemanager) <  %{zendframework_servicemanager_max_ver}
Requires:      php-autoloader(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver}
Requires:      php-autoloader(zendframework/zend-stdlib) <  %{zendframework_stdlib_max_ver}
Requires:      php-autoloader(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver}
Requires:      php-composer(zetacomponents/document) <  %{zetacomponents_document_max_ver}
Requires:      php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver}
Requires:      php-composer(webmozart/assert) < %{webmozart_assert_max_ver}
Requires:      php-composer(webmozart/assert) >= %{webmozart_assert_min_ver}
%endif
# phpcompatinfo (computed from version 2.9.1)
Requires:      php-date
Requires:      php-dom
Requires:      php-filter
Requires:      php-iconv
Requires:      php-igbinary
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
Requires:      php-xsl
Requires:      php-zlib
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-%{composer_project} = %{version}-%{release}
# Rename
Obsoletes:     php-pear-PhpDocumentor < 2.9.0-1
Provides:      php-pear-PhpDocumentor = %{version}-%{release}
Provides:      php-pear(PhpDocumentor) = %{version}
## This pkg was the only one in this channel so the channel is no longer needed
Obsoletes:     php-channel-phpdoc

# Bundled
## data/templates/abstract/js/jquery-1.4.2.min.js
## data/templates/old-ocean/js/jquery-1.4.2.min.js
## data/templates/responsive/js/jquery-1.4.2.min.js
Provides:      bundled(js-jquery) = 1.4.2
## data/templates/old-ocean/js/jquery-1.7.1.min.js
## data/templates/responsive/js/jquery-1.7.1.min.js
## docs/.static/js/jquery-1.7.1.min.js
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/jquery-1.7.1.min.js
Provides:      bundled(js-jquery) = 1.7.1
## data/templates/clean/js/jquery-1.11.0.min.js
Provides:      bundled(js-jquery) = 1.11.0
## data/templates/abstract/js/jquery-ui-1.8.2.custom.min.js
## data/templates/old-ocean/js/jquery-ui-1.8.2.custom.min.js
## data/templates/old-ocean/css/black-tie/jquery-ui-1.8.2.custom.css
## docs/.static/js/jquery-ui-1.8.2.custom.min.js
## data/templates/zend/css/black-tie/jquery-ui-1.8.2.custom.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/jquery-ui-1.8.2.custom.min.js
## data/templates/responsive/js/jquery-ui-1.8.2.custom.min.js
Provides:      bundled(js-jquery-ui) = 1.8.2
## data/templates/new-black/css/phpdoc/jquery-ui-1.8.16.custom.css
## data/templates/new-black/css/jquery-ui.css
Provides:      bundled(js-jquery-ui) = 1.8.16
## data/templates/clean/js/ui/1.10.4/jquery-ui.min.js
Provides:      bundled(js-jquery-ui) = 1.10.4
## data/templates/abstract/js/jquery.cookie.js
## data/templates/old-ocean/js/jquery.cookie.js
## data/templates/responsive/js/jquery.cookie.js
Provides:      bundled(js-jquery-cookie)
## data/templates/abstract/js/jquery.panzoom.js
## data/templates/old-ocean/js/jquery.panzoom.js
## data/templates/responsive/js/jquery.panzoom.js
Provides:      bundled(js-jquery-panzoom) = 0.9.0
## data/templates/abstract/js/jquery.tools.min.js
## data/templates/old-ocean/js/jquery.tools.min.js
## data/templates/responsive/js/jquery.tools.min.js
Provides:      bundled(js-jquery-tools) = 1.2.5
Provides:      bundled(js-jquery-event-wheel) = 1
## data/templates/abstract/js/jquery.treeview.js
## data/templates/old-ocean/js/jquery.treeview.js
## data/templates/responsive/js/jquery.treeview.js
Provides:      bundled(js-jquery-treeview) = 1.5
## data/templates/responsive/js/jquery.iviewer.js
## data/templates/responsive/js/jquery.iviewer.min.js
## data/templates/responsive/img/iviewer/*
Provides:      bundled(js-jquery-iviewer) = 0.7
## data/templates/clean/js/jquery.iviewer.js
## data/templates/clean/js/jquery.iviewer.min.js
Provides:      bundled(js-jquery-iviewer) = 0.7.7
## data/templates/clean/js/jquery.dotdotdot-1.5.9.js
## data/templates/clean/js/jquery.dotdotdot-1.5.9.min.js
Provides:      bundled(js-jquery-dotdotdot) = 1.5.9
## data/templates/responsive/js/jquery.mousewheel.min.js
Provides:      bundled(js-jquery-mousewheel) = 3.0.6
## data/templates/clean/js/jquery.mousewheel.js
Provides:      bundled(js-jquery-mousewheel) = 3.1.9
## data/templates/old-ocean/js/jquery.splitter.js
## data/templates/responsive/js/jquery.splitter.js
## data/templates/zend/js/jquery.splitter.js
Provides:      bundled(js-jquery-splitter) = 1.51
## data/templates/responsive/js/jquery.xml2json.js
Provides:      bundled(js-jquery-xml2json) = 1.3
## data/templates/responsive/js/jqplot/*
Provides:      bundled(js-jqplot) = 1.0.8
## data/templates/abstract/css/sen.full.min.css
Provides:      bundled(css-sencss)
## data/templates/clean/js/prism.min.js
## data/templates/clean/css/prism.css
Provides:      bundled(js-prism)
## data/templates/clean/css/font-awesome.min.css
## data/templates/clean/font/fontawesome-webfont.eot
## data/templates/clean/font/fontawesome-webfont.svg
## data/templates/clean/font/fontawesome-webfont.ttf
## data/templates/clean/font/fontawesome-webfont.woff
## data/templates/clean/font/FontAwesome.otf
Provides:      bundled(fontawesome) = 3.2.1
## data/templates/responsive/css/bootstrap.css
## data/templates/responsive/css/bootstrap.min.css
## data/templates/responsive/js/bootstrap.js
## data/templates/responsive/js/bootstrap.min.js
## docs/.static/css/bootstrap.min.css
## docs/.static/js/bootstrap.js
Provides:      bundled(js-bootstrap) = 2.0.0
## data/templates/clean/css/bootstrap-combined.no-icons.min.css
## data/templates/clean/js/bootstrap.min.js
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap-responsive.min.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap.min.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/bootstrap.min.js
Provides:      bundled(js-bootstrap) = 2.3.2
## data/templates/responsive/css/bootstrap-responsive.css
## data/templates/responsive/css/bootstrap-responsive.min.css
## docs/.static/css/bootstrap-responsive.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/bootstrap-responsive.css
Provides:      bundled(js-bootstrap-responsive) = 2.0.0
## data/templates/responsive/js/prettify/*
## docs/.static/css/prettify.css
## docs/.static/js/prettify/prettify.min.js
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/css/prettify.css
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/js/prettify/*
Provides:      bundled(js-prettify)
## data/templates/clean/js/html5.js
Provides:      bundled(js-html5) = 3.7.0
## data/templates/responsive/img/glyphicons-halflings-white.png
## data/templates/responsive/img/glyphicons-halflings.png
## docs/.static/img/glyphicons-halflings-white.png
## docs/.static/img/glyphicons-halflings.png
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/img/glyphicons-halflings-white.png
## src/phpDocumentor/Plugin/Scrybe/data/templates/default/img/glyphicons-halflings.png
Provides:      bundled(glyphicons-halflings)
## data/templates/old-ocean/js/SVGPan.js
## data/templates/responsive/js/SVGPan.js
Provides:      bundled(js-svgpan) = 1.2

%description
phpDocumentor is an application that is capable of analyzing your PHP source
code and DocBlock comments to generate a complete set of API Documentation.

Inspired by phpDocumentor 1 and JavaDoc it continues to innovate and is up to
date with the latest technologies and PHP language features.

Features: phpDocumentor supports the following:
* PHP 5.3 compatible, full support for Namespaces, Closures and more is provided
* Shows any tag, some tags add additional functionality to phpDocumentor
  (such as @link)
* Processing speed, Zend Framework experienced a significant reduction in
  processing time compared to phpDocumentor 1
* Low memory usage, peak memory usage for small projects is less than 20MB,
  medium projects 40MB and large frameworks 100MB
* Incremental parsing, if you kept the Structure file from a previous run you
  get an additional performance boost of up to 80% on top of the mentioned
  processing speed above
* Easy template building, if you want to make a branding you only have to call
  1 task and edit 3 files
* Command-line compatibility with phpDocumentor 1, phpDocumentor 2 is an
  application in its own right but the basic phpDocumentor 1 arguments,
  such as --directory, --file and --target, have been adopted
* Two-step process, phpDocumentor first generates a cache with your application
  structure before creating the output. If you'd like you can use that to power
  your own tools or formatters!


%prep
%setup -qn %{github_name}-%{github_commit}

sed -i 's#@package_version@#%{version}#' src/phpDocumentor/Application.php
echo -n "%{version}" > VERSION

: Adjust vendor dir
%patch0 -p1
sed -i 's#__PHPDIR__#%{phpdir}#' \
    bin/phpdoc \
    src/Cilex/Provider/JmsSerializerServiceProvider.php

: Adjust templates dir
%patch1 -p1

: E: zero-length
find . -type f -size 0 -delete -print

: E: script-without-shebang
chmod a-x src/phpDocumentor/Parser/File.php


%build
pushd src/phpDocumentor

: Create Fedora autoloader
cat <<'AUTOLOAD' | tee autoload-fedora.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('Cilex\\Provider\\', __DIR__.'/Cilex/Provider');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Cilex1/autoload.php',
    '%{phpdir}/erusev/parsedown/autoload.php',
    '%{phpdir}/ezc/Document/autoload.php',
    '%{phpdir}/JMS/Serializer/autoload.php',
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/phpDocumentor/Fileset/autoload.php',
    '%{phpdir}/phpDocumentor/GraphViz/autoload.php',
    '%{phpdir}/phpDocumentor/Reflection/autoload.php',
    '%{phpdir}/phpDocumentor/Reflection/DocBlock2/autoload.php',
    '%{phpdir}/Symfony/Component/Config/autoload.php',
    '%{phpdir}/Symfony/Component/Console/autoload.php',
    '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    '%{phpdir}/Symfony/Component/Process/autoload.php',
    '%{phpdir}/Symfony/Component/Stopwatch/autoload.php',
    '%{phpdir}/Symfony/Component/Validator/autoload.php',
    '%{phpdir}/Twig/autoload.php',
    '%{phpdir}/Zend/Cache/autoload.php',
    '%{phpdir}/Zend/Config/autoload.php',
    '%{phpdir}/Zend/Filter/autoload.php',
    '%{phpdir}/Zend/I18n/autoload.php',
    '%{phpdir}/Zend/Serializer/autoload.php',
    '%{phpdir}/Zend/ServiceManager/autoload.php',
    '%{phpdir}/Zend/Stdlib/autoload.php',
    '%{phpdir}/Webmozart/Assert/autoload.php',
));
AUTOLOAD

: Create custom composer.json for autoloader dump
cat <<'COMPOSER_JSON' | tee composer.json
{
    "autoload": {
        "files": [
            "autoload-fedora.php"
        ]
    }
}
COMPOSER_JSON

: Generate autoloader
composer dumpautoload --optimize

: Symlink autoloader
ln -s vendor/autoload.php autoload.php

: Cleanup
rm -f composer.json
popd

: Licenses
mkdir -p .rpm/licenses
mv LICENSE .rpm/licenses/
mkdir -p .rpm/licenses/vendor/composer
mv src/phpDocumentor/vendor/composer/LICENSE .rpm/licenses/vendor/composer/
mkdir -p .rpm/licenses/Plugin/Scrybe/
mv src/phpDocumentor/Plugin/Scrybe/docs/license.rst .rpm/licenses/Plugin/Scrybe/

: Docs
mkdir -p .rpm/docs
mv *.md composer.json .rpm/docs/
mkdir -p .rpm/docs/Plugin/LegacyNamespaceConverter
mv src/phpDocumentor/Plugin/LegacyNamespaceConverter/README.md .rpm/docs/Plugin/LegacyNamespaceConverter/
mv src/phpDocumentor/Plugin/Scrybe/docs .rpm/docs/Plugin/Scrybe
mv src/phpDocumentor/Plugin/Scrybe/README.md .rpm/docs/Plugin/Scrybe/


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src/phpDocumentor %{buildroot}%{phpdir}/
cp -rp src/Cilex %{buildroot}%{phpdir}/phpDocumentor/

: Data
cp -rp data %{buildroot}%{phpdir}/phpDocumentor/

: Bin
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/phpdoc %{buildroot}%{_bindir}/%{name}


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\', __DIR__.'/tests/unit/phpDocumentor');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Mockery/autoload.php',
    '%{phpdir}/org/bovigo/vfs/autoload.php',
    '%{phpdir}/Symfony/Component/ExpressionLanguage/autoload.php',
));
BOOTSTRAP

: Update mockery path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        # count(): Parameter must be an array or an object that implements Countable
        if [ $($PHP_EXEC -r 'echo PHP_VERSION_ID;') -ge 70200 ]; then
            sed 's/function testTypeIsInheritedWhenNoneIsPresent/function SKIP_testTypeIsInheritedWhenNoneIsPresent/' \
                -i tests/unit/phpDocumentor/Descriptor/ArgumentDescriptorTest.php
        fi

        $PHP_EXEC -d auto_prepend_file=%{buildroot}%{phpdir}/phpDocumentor/autoload-fedora.php \
            $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
# Library
%{phpdir}/phpDocumentor/Application.php
%{phpdir}/phpDocumentor/Bootstrap.php
%{phpdir}/phpDocumentor/Cilex
%{phpdir}/phpDocumentor/Command
%{phpdir}/phpDocumentor/Compiler
%{phpdir}/phpDocumentor/Configuration
%{phpdir}/phpDocumentor/Configuration.php
%{phpdir}/phpDocumentor/Console
%{phpdir}/phpDocumentor/Descriptor
%{phpdir}/phpDocumentor/Event
%{phpdir}/phpDocumentor/Parser
%{phpdir}/phpDocumentor/Partials
%{phpdir}/phpDocumentor/Plugin
%{phpdir}/phpDocumentor/Transformer
%{phpdir}/phpDocumentor/Translator
# Data
%{phpdir}/phpDocumentor/data
## Autoloaders
%{phpdir}/phpDocumentor/autoload-fedora.php
%{phpdir}/phpDocumentor/autoload.php
%{phpdir}/phpDocumentor/vendor
# Bin
%{_bindir}/%{name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn@iwin.ski> - 2.9.1-5
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1988067)
- Disable tests by default until update to v3

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep  7 2020 Remi Collet <remi@remirepo.net> - 2.9.1-2
- add dependency on webmozart/assert

* Sat Aug 29 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1
- fix zend-cache autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-7
- Use range dependencies
- Fix "PHP Warning: count(): Parameter must be an array or an object that
  implements Countable"
- Fix autoloader

* Wed Dec 27 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-6
- Add bundled provides

* Wed Nov 29 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-5
- Update license and add license breakdown

* Mon Nov 13 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-4
- Fix bin issues

* Sun Oct 01 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-3
- Fix BuildRequires
- Add php-cli dependencies
- Fix phpdocumentor/reflection-docblock autoload require

* Sun Sep 24 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-2
- Add missing virtual provide php-pear(PhpDocumentor)
- Fix rpmlint errors

* Sat Aug 19 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-1
- Initial package
