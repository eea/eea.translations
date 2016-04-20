eea.translations Package Readme
===============================

Overview
--------

Translations for EEA website. Most translations come from old local.eea.europa.eu website. We also have translated logos here.


Fixing templates and generate new pot and po files
--------------------------------------------------

1. go to your buildout home directory, e.g.:

    /var/local/deploy/eea-buildout-plone4

2. check templates for errors and generate the **eea.pot** file:

    $ tools/translate-check-i18ndude.sh

This script will generate a log with the directories scanned and the errors found. All the reported errors must be fixed.

**Important note**

In order to be able to successfully run tools/translate-check-i18ndude.sh the PT files that generates XML/RSS must be temporarily altered (more `details <http://trac.plumi.org/ticket/221>`_).

Right now (20.04.2016) there are 2 templates that will generate errors:

    TALError: empty HTML tags cannot use tal:content: 'link', at line 12, column 5, in file src/Products.EEAContentTypes/Products/EEAContentTypes/browser/rss.xml.pt
    
    TALError: empty HTML tags cannot use tal:content: 'link', at line 22, column 3, in file src/Products.EEAContentTypes/Products/EEAContentTypes/skins/EEAContentTypes_public/rss_template.pt

To generate the **eea.pot** file you must temporarily change all the <link> tags to something like <linka>; after the file generation switch back.

3. generate the **po** files:

    $ tools/translate-generate-po.sh

4. start your www1 in debug mode

    $ bin/www1 fg

and check to see there are no warnings like:

    2016-04-19 10:58:33 WARNING zope.i18n Error while compiling /var/local/deploy/eea-buildout-plone4/src/eea.translations/eea/translations/locales/it/LC_MESSAGES/eea.po

If there are such warinings, stop www1 and:

    $ cd src/eea.translations/eea/translations/locales/ 
    
    $ ./generate-mo.sh

This script will display the po files with error indicated the exact message, e.g.

    bg/LC_MESSAGES/eea.po:3238: keyword "$" unknown

In this case the indicated po file must be opened in your editor; go to that line (3228) and see what message caused the error and where it comes from. After fixging all the errors repeat the process.


5. use your text editor or `Poedit <https://poedit.net/download>`_ to update the translations in the po files.

Sometimes, it happens that a message is missing from a PO file, let's say the one for Italian (it). In that case, a manual sync must be done:

    $ cd src/eea.translations/eea/translations/locales/
    
    $ /var/local/deploy/eea-buildout-plone4/bin/i18ndude sync --pot eea.pot  it/LC_MESSAGES/eea.po
    
    $ it/LC_MESSAGES/eea.po: 102 added, 84 removed

After that, reload the PO file and try again.

6. `HowToManageTranslations <https://taskman.eionet.europa.eu/projects/content/wiki/HowToManageTranslations>`_
