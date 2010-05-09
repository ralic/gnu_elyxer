#! /usr/bin/env python
# -*- coding: utf-8 -*-

# eLyXer configuration
# autogenerated from config file on 2010-05-10

class BibStylesConfig(object):
  "Configuration class from config file"

  abbrvnat = {
      
      u'@article':u'$author. $title. <i>$journal</i>,{ {$volume:}$pages,} $month $year.{ doi: $doi.}{ URL $url.}', 
      u'cite':[u'$surname($year)',u'$rest',], 
      u'default':u'$author. <i>$title</i>. $publisher, $year.', 
      }

  authordate2 = {
      
      u'@article':u'$author. $year. $title. <i>$journal</i>, <b>$volume</b>($number), $pages.', 
      u'@book':u'$author. $year. <i>$title</i>. $publisher.', 
      u'cite':[u'$surname',u' $year; $rest',], 
      u'default':u'$author. $year. <i>$title</i>. $publisher.', 
      }

  default = {
      u'@article':u'$author, “$title”, <i>$journal</i>, pp. $pages, $year.', 
      u'@book':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@booklet':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@conference':u'$author, “$title”, <i>$journal</i>, pp. $pages, $year.', 
      u'@inbook':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@incollection':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@inproceedings':u'$author, “$title”, <i>$journal</i>, pp. $pages, $year.', 
      u'@manual':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@mastersthesis':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@misc':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@phdthesis':u'$author, <i>$title</i>. $publisher, $year.', 
      u'@proceedings':u'$author, “$title”, <i>$journal</i>, pp. $pages, $year.', 
      u'@techreport':u'$author, <i>$title</i>, $year.', 
      u'@unpublished':u'$author, “$title”, <i>$journal</i>, $year.', 
      u'cite':[u'$index',u'$rest',], 
      u'default':u'$author, <i>$title</i>. $publisher, $year.', 
      }

  ieeetr = {
      
      u'@article':u'$author, “$title”, <i>$journal</i>, vol. $volume, no. $number, pp. $pages, $year.', 
      u'@book':u'$author, <i>$title</i>. $publisher, $year.', 
      u'cite':[u'$index',u'$rest',], 
      }

  plain = {
      
      u'@article':u'$author. $title. <i>$journal</i>, $volumen($number):$pages, $year.', 
      u'@book':u'$author. <i>$title</i>. $publisher, $month $year.', 
      u'cite':[u'$index',u'$rest',], 
      u'default':u'$author. <i>$title</i>. $publisher, $year.', 
      }

class BibTeXConfig(object):
  "Configuration class from config file"

  escaped = {
      u'--':u'—', u'..':u'.', u'\\"a':u'ä', u'\\"e':u'ë', u'\\"i':u'ï', 
      u'\\"o':u'ö', u'\\"u':u'ü', 
      }

class ContainerConfig(object):
  "Configuration class from config file"

  endings = {
      u'Align':u'\\end_layout', u'BarredText':u'\\bar', 
      u'BoldText':u'\\series', u'Cell':u'</cell', u'ColorText':u'\\color', 
      u'EmphaticText':u'\\emph', u'Hfill':u'\\hfill', u'Inset':u'\\end_inset', 
      u'Layout':u'\\end_layout', u'LyXFooter':u'\\end_document', 
      u'LyXHeader':u'\\end_header', u'Row':u'</row', u'ShapedText':u'\\shape', 
      u'SizeText':u'\\size', u'TextFamily':u'\\family', 
      u'VersalitasText':u'\\noun', 
      }

  startendings = {
      u'\\begin_deeper':u'\\end_deeper', u'\\begin_inset':u'\\end_inset', 
      u'\\begin_layout':u'\\end_layout', 
      }

  starts = {
      u'':u'StringContainer', u'#LyX':u'BlackBox', u'</lyxtabular':u'BlackBox', 
      u'<cell':u'Cell', u'<column':u'Column', u'<row':u'Row', 
      u'\\align':u'Align', u'\\bar':u'BarredText', 
      u'\\bar default':u'BlackBox', u'\\bar no':u'BlackBox', 
      u'\\begin_body':u'BlackBox', u'\\begin_deeper':u'DeeperList', 
      u'\\begin_document':u'BlackBox', u'\\begin_header':u'LyXHeader', 
      u'\\begin_inset Box':u'BoxInset', u'\\begin_inset Branch':u'Branch', 
      u'\\begin_inset Caption':u'Caption', 
      u'\\begin_inset CommandInset bibitem':u'BiblioEntry', 
      u'\\begin_inset CommandInset bibtex':u'BibTeX', 
      u'\\begin_inset CommandInset citation':u'BiblioCitation', 
      u'\\begin_inset CommandInset href':u'URL', 
      u'\\begin_inset CommandInset include':u'IncludeInset', 
      u'\\begin_inset CommandInset index_print':u'PrintIndex', 
      u'\\begin_inset CommandInset label':u'Label', 
      u'\\begin_inset CommandInset nomencl_print':u'PrintNomenclature', 
      u'\\begin_inset CommandInset nomenclature':u'NomenclatureEntry', 
      u'\\begin_inset CommandInset ref':u'Reference', 
      u'\\begin_inset CommandInset toc':u'TableOfContents', 
      u'\\begin_inset ERT':u'ERT', u'\\begin_inset Flex':u'FlexInset', 
      u'\\begin_inset Flex Chunkref':u'NewfangledChunkRef', 
      u'\\begin_inset Flex Marginnote':u'SideNote', 
      u'\\begin_inset Flex Sidenote':u'SideNote', 
      u'\\begin_inset Flex URL':u'FlexURL', u'\\begin_inset Float':u'Float', 
      u'\\begin_inset FloatList':u'ListOf', u'\\begin_inset Foot':u'Footnote', 
      u'\\begin_inset Formula':u'Formula', 
      u'\\begin_inset FormulaMacro':u'FormulaMacro', 
      u'\\begin_inset Graphics':u'Image', u'\\begin_inset Index':u'IndexEntry', 
      u'\\begin_inset Info':u'InfoInset', 
      u'\\begin_inset LatexCommand bibitem':u'BiblioEntry', 
      u'\\begin_inset LatexCommand bibtex':u'BibTeX', 
      u'\\begin_inset LatexCommand cite':u'BiblioCitation', 
      u'\\begin_inset LatexCommand citealt':u'BiblioCitation', 
      u'\\begin_inset LatexCommand citep':u'BiblioCitation', 
      u'\\begin_inset LatexCommand citet':u'BiblioCitation', 
      u'\\begin_inset LatexCommand htmlurl':u'URL', 
      u'\\begin_inset LatexCommand index':u'IndexEntry', 
      u'\\begin_inset LatexCommand label':u'Label', 
      u'\\begin_inset LatexCommand nomenclature':u'NomenclatureEntry', 
      u'\\begin_inset LatexCommand prettyref':u'Reference', 
      u'\\begin_inset LatexCommand printindex':u'PrintIndex', 
      u'\\begin_inset LatexCommand printnomenclature':u'PrintNomenclature', 
      u'\\begin_inset LatexCommand ref':u'Reference', 
      u'\\begin_inset LatexCommand tableofcontents':u'TableOfContents', 
      u'\\begin_inset LatexCommand url':u'URL', 
      u'\\begin_inset LatexCommand vref':u'Reference', 
      u'\\begin_inset Marginal':u'SideNote', 
      u'\\begin_inset Newline':u'NewlineInset', 
      u'\\begin_inset Newpage':u'NewPageInset', u'\\begin_inset Note':u'Note', 
      u'\\begin_inset OptArg':u'ShortTitle', 
      u'\\begin_inset Quotes':u'QuoteContainer', 
      u'\\begin_inset Tabular':u'Table', u'\\begin_inset Text':u'InsetText', 
      u'\\begin_inset VSpace':u'VerticalSpace', u'\\begin_inset Wrap':u'Wrap', 
      u'\\begin_inset listings':u'Listing', u'\\begin_inset space':u'Space', 
      u'\\begin_layout':u'Layout', u'\\begin_layout Abstract':u'Abstract', 
      u'\\begin_layout Author':u'Author', 
      u'\\begin_layout Bibliography':u'Bibliography', 
      u'\\begin_layout Chunk':u'NewfangledChunk', 
      u'\\begin_layout Description':u'Description', 
      u'\\begin_layout Enumerate':u'ListItem', 
      u'\\begin_layout Itemize':u'ListItem', u'\\begin_layout List':u'List', 
      u'\\begin_layout LyX-Code':u'LyXCode', 
      u'\\begin_layout Plain':u'PlainLayout', 
      u'\\begin_layout Standard':u'StandardLayout', 
      u'\\begin_layout Title':u'Title', u'\\color':u'ColorText', 
      u'\\color inherit':u'BlackBox', u'\\color none':u'BlackBox', 
      u'\\emph default':u'BlackBox', u'\\emph off':u'BlackBox', 
      u'\\emph on':u'EmphaticText', u'\\emph toggle':u'EmphaticText', 
      u'\\end_body':u'LyXFooter', u'\\family':u'TextFamily', 
      u'\\family default':u'BlackBox', u'\\family roman':u'BlackBox', 
      u'\\hfill':u'Hfill', u'\\labelwidthstring':u'BlackBox', 
      u'\\lang':u'LangLine', u'\\length':u'BlackBox', 
      u'\\lyxformat':u'LyXFormat', u'\\lyxline':u'LyXLine', 
      u'\\newline':u'Newline', u'\\newpage':u'NewPage', 
      u'\\noindent':u'BlackBox', u'\\noun default':u'BlackBox', 
      u'\\noun off':u'BlackBox', u'\\noun on':u'VersalitasText', 
      u'\\paragraph_spacing':u'BlackBox', u'\\series bold':u'BoldText', 
      u'\\series default':u'BlackBox', u'\\series medium':u'BlackBox', 
      u'\\shape':u'ShapedText', u'\\shape default':u'BlackBox', 
      u'\\shape up':u'BlackBox', u'\\size':u'SizeText', 
      u'\\size normal':u'BlackBox', u'\\start_of_appendix':u'Appendix', 
      }

  string = {
      u'startcommand':u'\\', 
      }

  table = {
      u'headers':[u'<lyxtabular',u'<features',], 
      }

class EscapeConfig(object):
  "Configuration class from config file"

  chars = {
      u'\n':u'', u' -- ':u' — ', u'\'':u'’', u'---':u'—', u'`':u'‘', 
      }

  commands = {
      u'\\InsetSpace \\space{}':u' ', u'\\InsetSpace \\thinspace{}':u' ', 
      u'\\InsetSpace ~':u' ', u'\\SpecialChar \\-':u'', 
      u'\\SpecialChar \\@.':u'.', u'\\SpecialChar \\ldots{}':u'…', 
      u'\\SpecialChar \\menuseparator':u' ▷ ', 
      u'\\SpecialChar \\nobreakdash-':u'-', u'\\SpecialChar \\slash{}':u'/', 
      u'\\SpecialChar \\textcompwordmark{}':u'', u'\\backslash':u'\\', 
      }

  entities = {
      u'&':u'&amp;', u'<':u'&lt;', u'>':u'&gt;', 
      }

  html = {
      u'/>':u'>', 
      }

  iso885915 = {
      u' ':u'&nbsp;', u' ':u'&emsp;', u' ':u'&#8197;', 
      }

  nonunicode = {
      u' ':u' ', 
      }

class FileConfig(object):
  "Configuration class from config file"

  parsing = {
      u'encodings':[u'utf-8',u'Cp1252',], 
      }

class FootnoteConfig(object):
  "Configuration class from config file"

  constants = {
      u'postfrom':u'] ', u'postto':u'→] ', u'prefrom':u'[→', u'preto':u' [', 
      }

class FormulaConfig(object):
  "Configuration class from config file"

  alphacommands = {
      u'\\AA':u'Å', u'\\AE':u'Æ', u'\\L':u'Ł', u'\\O':u'Ø', u'\\OE':u'Œ', 
      u'\\aa':u'å', u'\\ae':u'æ', u'\\alpha':u'α', u'\\beta':u'β', 
      u'\\delta':u'δ', u'\\epsilon':u'ϵ', u'\\eta':u'η', u'\\gamma':u'γ', 
      u'\\iota':u'ι', u'\\kappa':u'κ', u'\\l':u'ł', u'\\lambda':u'λ', 
      u'\\mu':u'μ', u'\\nu':u'ν', u'\\o':u'ø', u'\\oe':u'œ', u'\\omega':u'ω', 
      u'\\phi':u'φ', u'\\pi':u'π', u'\\psi':u'ψ', u'\\rho':u'ρ', 
      u'\\sigma':u'σ', u'\\ss':u'ß', u'\\tau':u'τ', u'\\textcrh':u'ħ', 
      u'\\theta':u'θ', u'\\upsilon':u'υ', u'\\varDelta':u'∆', 
      u'\\varGamma':u'Γ', u'\\varLambda':u'Λ', u'\\varOmega':u'Ω', 
      u'\\varPhi':u'Φ', u'\\varPi':u'Π', u'\\varPsi':u'Ψ', u'\\varSigma':u'Σ', 
      u'\\varTheta':u'Θ', u'\\varUpsilon':u'Υ', u'\\varXi':u'Ξ', 
      u'\\varepsilon':u'ε', u'\\varkappa':u'ϰ', u'\\varphi':u'φ', 
      u'\\varpi':u'ϖ', u'\\varrho':u'ϱ', u'\\varsigma':u'ς', 
      u'\\vartheta':u'ϑ', u'\\xi':u'ξ', u'\\zeta':u'ζ', 
      }

  array = {
      u'begin':u'\\begin', u'cellseparator':u'&', u'end':u'\\end', 
      u'rowseparator':u'\\\\', 
      }

  commands = {
      u'\\ ':u' ', u'\\!':u'', u'\\$':u'$', u'\\%':u'%', u'\\,':u' ', 
      u'\\:':u' ', u'\\;':u' ', u'\\APLdownarrowbox':u'⍗', 
      u'\\APLleftarrowbox':u'⍇', u'\\APLrightarrowbox':u'⍈', 
      u'\\APLuparrowbox':u'⍐', u'\\Box':u'□', u'\\Bumpeq':u'≎', 
      u'\\CIRCLE':u'●', u'\\Cap':u'⋒', u'\\CheckedBox':u'☑', u'\\Circle':u'○', 
      u'\\Coloneqq':u'⩴', u'\\Corresponds':u'≙', u'\\Cup':u'⋓', 
      u'\\Delta':u'Δ', u'\\Diamond':u'◇', u'\\Downarrow':u'⇓', u'\\EUR':u'€', 
      u'\\Gamma':u'Γ', u'\\Im':u'ℑ', u'\\Join':u'⨝', u'\\LEFTCIRCLE':u'◖', 
      u'\\LEFTcircle':u'◐', u'\\Lambda':u'Λ', u'\\Leftarrow':u'⇐', 
      u'\\Leftrightarrow':u' ⇔ ', u'\\Lleftarrow':u'⇚', 
      u'\\Longleftarrow':u'⟸', u'\\Longleftrightarrow':u'⟺', 
      u'\\Longrightarrow':u'⟹', u'\\Lsh':u'↰', u'\\Mapsfrom':u'⇐|', 
      u'\\Mapsto':u'|⇒', u'\\Omega':u'Ω', u'\\P':u'¶', u'\\Phi':u'Φ', 
      u'\\Pi':u'Π', u'\\Pr':u'Pr', u'\\Psi':u'Ψ', u'\\RIGHTCIRCLE':u'◗', 
      u'\\RIGHTcircle':u'◑', u'\\Re':u'ℜ', u'\\Rightarrow':u' ⇒ ', 
      u'\\Rrightarrow':u'⇛', u'\\Rsh':u'↱', u'\\S':u'§', u'\\Sigma':u'Σ', 
      u'\\Square':u'☐', u'\\Subset':u'⋐', u'\\Supset':u'⋑', u'\\Theta':u'Θ', 
      u'\\Uparrow':u'⇑', u'\\Updownarrow':u'⇕', u'\\Upsilon':u'Υ', 
      u'\\Vdash':u'⊩', u'\\Vert':u'∥', u'\\Vvdash':u'⊪', u'\\XBox':u'☒', 
      u'\\Xi':u'Ξ', u'\\Yup':u'⅄', u'\\\\':u'<br/>', u'\\_':u'_', 
      u'\\aleph':u'ℵ', u'\\amalg':u'∐', u'\\angle':u'∠', u'\\approx':u' ≈ ', 
      u'\\aquarius':u'♒', u'\\arccos':u'arccos', u'\\arcsin':u'arcsin', 
      u'\\arctan':u'arctan', u'\\arg':u'arg', u'\\aries':u'♈', u'\\ast':u'∗', 
      u'\\asymp':u'≍', u'\\backepsilon':u'∍', u'\\backprime':u'‵', 
      u'\\backsimeq':u'⋍', u'\\backslash':u'\\', u'\\barwedge':u'⊼', 
      u'\\because':u'∵', u'\\beth':u'ℶ', u'\\between':u'≬', u'\\bigcap':u'∩', 
      u'\\bigcirc':u'○', u'\\bigcup':u'∪', u'\\bigodot':u'⊙', 
      u'\\bigoplus':u'⊕', u'\\bigotimes':u'⊗', u'\\bigsqcup':u'⊔', 
      u'\\bigstar':u'★', u'\\bigtriangledown':u'▽', u'\\bigtriangleup':u'△', 
      u'\\biguplus':u'⊎', u'\\bigvee':u'∨', u'\\bigwedge':u'∧', 
      u'\\blacklozenge':u'⧫', u'\\blacksmiley':u'☻', u'\\blacksquare':u'■', 
      u'\\blacktriangle':u'▲', u'\\blacktriangledown':u'▼', 
      u'\\blacktriangleright':u'▶', u'\\bot':u'⊥', u'\\bowtie':u'⋈', 
      u'\\box':u'▫', u'\\boxdot':u'⊡', u'\\bullet':u'•', u'\\bumpeq':u'≏', 
      u'\\cancer':u'♋', u'\\cap':u'∩', u'\\capricornus':u'♑', u'\\cdot':u'⋅', 
      u'\\cdots':u'⋯', u'\\centerdot':u'∙', u'\\checkmark':u'✓', u'\\chi':u'χ', 
      u'\\circ':u'○', u'\\circeq':u'≗', u'\\circledR':u'®', 
      u'\\circledast':u'⊛', u'\\circledcirc':u'⊚', u'\\circleddash':u'⊝', 
      u'\\clubsuit':u'♣', u'\\coloneqq':u'≔', u'\\complement':u'∁', 
      u'\\cong':u'≅', u'\\coprod':u'∐', u'\\copyright':u'©', u'\\cos':u'cos', 
      u'\\cosh':u'cosh', u'\\cot':u'cot', u'\\coth':u'coth', u'\\csc':u'csc', 
      u'\\cup':u'∪', u'\\curvearrowleft':u'↶', u'\\curvearrowright':u'↷', 
      u'\\dag':u'†', u'\\dagger':u'†', u'\\daleth':u'ℸ', 
      u'\\dashleftarrow':u'⇠', u'\\dashrightarrow':u' ⇢ ', u'\\dashv':u'⊣', 
      u'\\ddag':u'‡', u'\\ddagger':u'‡', u'\\ddots':u'⋱', u'\\deg':u'deg', 
      u'\\det':u'det', u'\\diagdown':u'╲', u'\\diagup':u'╱', u'\\diamond':u'◇', 
      u'\\diamondsuit':u'♦', u'\\dim':u'dim', u'\\displaystyle':u'', 
      u'\\div':u'÷', u'\\divideontimes':u'⋇', u'\\dotdiv':u'∸', 
      u'\\doteq':u'≐', u'\\doteqdot':u'≑', u'\\dotplus':u'∔', u'\\dots':u'…', 
      u'\\doublebarwedge':u'⌆', u'\\downarrow':u'↓', u'\\downdownarrows':u'⇊', 
      u'\\downharpoonleft':u'⇃', u'\\downharpoonright':u'⇂', u'\\earth':u'♁', 
      u'\\ell':u'ℓ', u'\\emptyset':u'∅', u'\\eqcirc':u'≖', u'\\eqcolon':u'≕', 
      u'\\eqsim':u'≂', u'\\equiv':u' ≡ ', u'\\euro':u'€', u'\\exists':u'∃', 
      u'\\exp':u'exp', u'\\fallingdotseq':u'≒', u'\\female':u'♀', 
      u'\\flat':u'♭', u'\\forall':u'∀', u'\\frown':u'⌢', u'\\frownie':u'☹', 
      u'\\gcd':u'gcd', u'\\ge':u' ≥ ', u'\\gemini':u'♊', u'\\geq':u' ≥ ', 
      u'\\geq)':u'≥', u'\\geqq':u'≧', u'\\geqslant':u'≥', u'\\gets':u'←', 
      u'\\gg':u'≫', u'\\ggg':u'⋙', u'\\gimel':u'ℷ', u'\\gneqq':u'≩', 
      u'\\gnsim':u'⋧', u'\\gtrdot':u'⋗', u'\\gtreqless':u'⋚', 
      u'\\gtreqqless':u'⪌', u'\\gtrless':u'≷', u'\\gtrsim':u'≳', 
      u'\\hbar':u'ℏ', u'\\heartsuit':u'♥', 
      u'\\hfill':u'<span class="hfill"> </span>', u'\\hom':u'hom', 
      u'\\hookleftarrow':u'↩', u'\\hookrightarrow':u'↪', u'\\hslash':u'ℏ', 
      u'\\idotsint':u'∫⋯∫', u'\\iiint':u'∭', u'\\iint':u'∬', u'\\imath':u'ı', 
      u'\\implies':u'  ⇒  ', u'\\in':u' ∈ ', u'\\inf':u'inf', u'\\infty':u'∞', 
      u'\\int':u'<span class="bigsymbol">∫</span>', 
      u'\\intop':u'<span class="bigsymbol">∫</span>', u'\\invneg':u'⌐', 
      u'\\jmath':u'ȷ', u'\\jupiter':u'♃', u'\\ker':u'ker', u'\\land':u'∧', 
      u'\\landupint':u'∱', u'\\langle':u'⟨', u'\\lbrace':u'{', 
      u'\\lbrace)':u'{', u'\\lbrack':u'[', u'\\lceil':u'⌈', u'\\ldots':u'…', 
      u'\\le':u'≤', u'\\leadsto':u'⇝', u'\\leftarrow':u' ← ', 
      u'\\leftarrow)':u'←', u'\\leftarrowtail':u'↢', u'\\leftarrowtobar':u'⇤', 
      u'\\leftharpoondown':u'↽', u'\\leftharpoonup':u'↼', 
      u'\\leftleftarrows':u'⇇', u'\\leftleftharpoons':u'⥢', u'\\leftmoon':u'☾', 
      u'\\leftrightarrow':u'↔', u'\\leftrightarrows':u'⇆', 
      u'\\leftrightharpoons':u'⇋', u'\\leftthreetimes':u'⋋', u'\\leo':u'♌', 
      u'\\leq':u' ≤ ', u'\\leq)':u'≤', u'\\leqq':u'≦', u'\\leqslant':u'≤', 
      u'\\lessdot':u'⋖', u'\\lesseqgtr':u'⋛', u'\\lesseqqgtr':u'⪋', 
      u'\\lessgtr':u'≶', u'\\lesssim':u'≲', u'\\lfloor':u'⌊', u'\\lg':u'lg', 
      u'\\lhd':u'⊲', u'\\libra':u'♎', u'\\lightning':u'↯', u'\\lim':u'lim', 
      u'\\liminf':u'liminf', u'\\limsup':u'limsup', u'\\ll':u'≪', 
      u'\\lll':u'⋘', u'\\ln':u'ln', u'\\lneqq':u'≨', u'\\lnot':u'¬', 
      u'\\lnsim':u'⋦', u'\\log':u'log', u'\\longleftarrow':u'⟵', 
      u'\\longleftrightarrow':u'⟷', u'\\longmapsto':u'⟼', 
      u'\\longrightarrow':u'⟶', u'\\looparrowleft':u'↫', 
      u'\\looparrowright':u'↬', u'\\lor':u'∨', u'\\lozenge':u'◊', 
      u'\\ltimes':u'⋉', u'\\lyxlock':u'', u'\\male':u'♂', u'\\maltese':u'✠', 
      u'\\mapsfrom':u'↤', u'\\mapsto':u'↦', u'\\mathcircumflex':u'^', 
      u'\\max':u'max', u'\\measuredangle':u'∡', u'\\mercury':u'☿', 
      u'\\mho':u'℧', u'\\mid':u'∣', u'\\min':u'min', u'\\models':u'⊨', 
      u'\\mp':u'∓', u'\\multimap':u'⊸', u'\\nLeftarrow':u'⇍', 
      u'\\nLeftrightarrow':u'⇎', u'\\nRightarrow':u'⇏', u'\\nVDash':u'⊯', 
      u'\\nabla':u'∇', u'\\napprox':u'≉', u'\\natural':u'♮', u'\\ncong':u'≇', 
      u'\\ne':u' ≠ ', u'\\nearrow':u'↗', u'\\neg':u'¬', u'\\neg)':u'¬', 
      u'\\neptune':u'♆', u'\\neq':u' ≠ ', u'\\nequiv':u'≢', u'\\nexists':u'∄', 
      u'\\ngeqslant':u'≱', u'\\ngtr':u'≯', u'\\ngtrless':u'≹', u'\\ni':u'∋', 
      u'\\ni)':u'∋', u'\\nleftarrow':u'↚', u'\\nleftrightarrow':u'↮', 
      u'\\nleqslant':u'≰', u'\\nless':u'≮', u'\\nlessgtr':u'≸', u'\\nmid':u'∤', 
      u'\\nonumber':u'', u'\\not':u'¬', u'\\not<':u'≮', u'\\not=':u'≠', 
      u'\\not>':u'≯', u'\\not\\in':u' ∉ ', u'\\notbackslash':u'⍀', 
      u'\\notin':u'∉', u'\\notni':u'∌', u'\\notslash':u'⌿', 
      u'\\nparallel':u'∦', u'\\nprec':u'⊀', u'\\nrightarrow':u'↛', 
      u'\\nsim':u'≁', u'\\nsimeq':u'≄', u'\\nsqsubset':u'⊏̸', 
      u'\\nsubseteq':u'⊈', u'\\nsucc':u'⊁', u'\\nsucccurlyeq':u'⋡', 
      u'\\nsupset':u'⊅', u'\\nsupseteq':u'⊉', u'\\ntriangleleft':u'⋪', 
      u'\\ntrianglelefteq':u'⋬', u'\\ntriangleright':u'⋫', 
      u'\\ntrianglerighteq':u'⋭', u'\\nvDash':u'⊭', u'\\nvdash':u'⊬', 
      u'\\nwarrow':u'↖', u'\\odot':u'⊙', u'\\oiiint':u'∰', u'\\oiint':u'∯', 
      u'\\oint':u'∮', u'\\ointclockwise':u'∲', u'\\ointctrclockwise':u'∳', 
      u'\\ominus':u'⊖', u'\\oplus':u'⊕', u'\\oslash':u'⊘', u'\\otimes':u'⊗', 
      u'\\owns':u'∋', u'\\parallel':u'∥', u'\\partial':u'∂', u'\\perp':u'⊥', 
      u'\\pisces':u'♓', u'\\pitchfork':u'⋔', u'\\pluto':u'♇', u'\\pm':u'±', 
      u'\\pointer':u'➪', u'\\pounds':u'£', u'\\prec':u'≺', 
      u'\\preccurlyeq':u'≼', u'\\preceq':u'≼', u'\\precsim':u'≾', 
      u'\\prime':u'′', u'\\prod':u'<span class="bigsymbol">∏</span>', 
      u'\\prompto':u'∝', u'\\propto':u' ∝ ', u'\\qquad':u'  ', u'\\quad':u' ', 
      u'\\quarternote':u'♩', u'\\rangle':u'⟩', u'\\rbrace':u'}', 
      u'\\rbrace)':u'}', u'\\rbrack':u']', u'\\rceil':u'⌉', u'\\rfloor':u'⌋', 
      u'\\rhd':u'⊳', u'\\rightarrow':u' → ', u'\\rightarrow)':u'→', 
      u'\\rightarrowtail':u'↣', u'\\rightarrowtobar':u'⇥', 
      u'\\rightharpoondown':u'⇁', u'\\rightharpoonup':u'⇀', 
      u'\\rightharpooondown':u'⇁', u'\\rightharpooonup':u'⇀', 
      u'\\rightleftarrows':u'⇄', u'\\rightleftharpoons':u'⇌', 
      u'\\rightmoon':u'☽', u'\\rightrightarrows':u'⇉', 
      u'\\rightrightharpoons':u'⥤', u'\\rightsquigarrow':u' ⇝ ', 
      u'\\rightthreetimes':u'⋌', u'\\risingdotseq':u'≓', u'\\rtimes':u'⋊', 
      u'\\sagittarius':u'♐', u'\\saturn':u'♄', u'\\scorpio':u'♏', 
      u'\\scriptscriptstyle':u'', u'\\scriptstyle':u'', u'\\searrow':u'↘', 
      u'\\sec':u'sec', u'\\setminus':u'∖', u'\\sharp':u'♯', u'\\sim':u' ~ ', 
      u'\\simeq':u'≃', u'\\sin':u'sin', u'\\sinh':u'sinh', u'\\slash':u'∕', 
      u'\\smile':u'⌣', u'\\smiley':u'☺', u'\\spadesuit':u'♠', 
      u'\\sphericalangle':u'∢', u'\\sqcap':u'⊓', u'\\sqcup':u'⊔', 
      u'\\sqsubset':u'⊏', u'\\sqsubseteq':u'⊑', u'\\sqsupset':u'⊐', 
      u'\\sqsupseteq':u'⊒', u'\\square':u'□', u'\\star':u'⋆', 
      u'\\subset':u' ⊂ ', u'\\subseteq':u'⊆', u'\\subseteqq':u'⫅', 
      u'\\subsetneqq':u'⫋', u'\\succ':u'≻', u'\\succcurlyeq':u'≽', 
      u'\\succeq':u'≽', u'\\succnsim':u'⋩', u'\\succsim':u'≿', 
      u'\\sum':u'<span class="bigsymbol">∑</span>', u'\\sun':u'☼', 
      u'\\sup':u'sup', u'\\supset':u' ⊃ ', u'\\supseteq':u'⊇', 
      u'\\supseteqq':u'⫆', u'\\supsetneqq':u'⫌', u'\\surd':u'√', 
      u'\\swarrow':u'↙', u'\\tan':u'tan', u'\\tanh':u'tanh', u'\\taurus':u'♉', 
      u'\\textbackslash':u'\\', u'\\textstyle':u'', u'\\therefore':u'∴', 
      u'\\times':u' × ', u'\\to':u'→', u'\\top':u'⊤', u'\\triangle':u'△', 
      u'\\triangleleft':u'⊲', u'\\trianglelefteq':u'⊴', u'\\triangleq':u'≜', 
      u'\\triangleright':u'▷', u'\\trianglerighteq':u'⊵', 
      u'\\twoheadleftarrow':u'↞', u'\\twoheadrightarrow':u'↠', 
      u'\\twonotes':u'♫', u'\\udot':u'⊍', u'\\unlhd':u'⊴', u'\\unrhd':u'⊵', 
      u'\\unrhl':u'⊵', u'\\uparrow':u'↑', u'\\updownarrow':u'↕', 
      u'\\upharpoonleft':u'↿', u'\\upharpoonright':u'↾', u'\\uplus':u'⊎', 
      u'\\upuparrows':u'⇈', u'\\uranus':u'♅', u'\\vDash':u'⊨', 
      u'\\varclubsuit':u'♧', u'\\vardiamondsuit':u'♦', u'\\varheartsuit':u'♥', 
      u'\\varnothing':u'∅', u'\\varspadesuit':u'♤', u'\\vdash':u'⊢', 
      u'\\vdots':u'⋮', u'\\vee':u'∨', u'\\vee)':u'∨', u'\\veebar':u'⊻', 
      u'\\vert':u'∣', u'\\virgo':u'♍', u'\\wedge':u'∧', u'\\wedge)':u'∧', 
      u'\\wp':u'℘', u'\\wr':u'≀', u'\\yen':u'¥', u'\\{':u'{', u'\\|':u'∥', 
      u'\\}':u'}', 
      }

  decoratingfunctions = {
      u'\\acute':u'´', u'\\acute{A}':u'Á', u'\\acute{C}':u'Ć', 
      u'\\acute{E}':u'É', u'\\acute{G}':u'Ǵ', u'\\acute{I}':u'Í', 
      u'\\acute{K}':u'Ḱ', u'\\acute{L}':u'Ĺ', u'\\acute{M}':u'Ḿ', 
      u'\\acute{N}':u'Ń', u'\\acute{O}':u'Ó', u'\\acute{P}':u'Ṕ', 
      u'\\acute{R}':u'Ŕ', u'\\acute{S}':u'Ś', u'\\acute{U}':u'Ú', 
      u'\\acute{W}':u'Ẃ', u'\\acute{Y}':u'Ý', u'\\acute{Z}':u'Ź', 
      u'\\acute{a}':u'á', u'\\acute{c}':u'ć', u'\\acute{e}':u'é', 
      u'\\acute{g}':u'ǵ', u'\\acute{i}':u'í', u'\\acute{k}':u'ḱ', 
      u'\\acute{l}':u'ĺ', u'\\acute{m}':u'ḿ', u'\\acute{n}':u'ń', 
      u'\\acute{o}':u'ó', u'\\acute{p}':u'ṕ', u'\\acute{r}':u'ŕ', 
      u'\\acute{s}':u'ś', u'\\acute{u}':u'ú', u'\\acute{w}':u'ẃ', 
      u'\\acute{y}':u'ý', u'\\acute{z}':u'ź', u'\\bar{A}':u'Ā', 
      u'\\bar{E}':u'Ē', u'\\bar{I}':u'Ī', u'\\bar{O}':u'Ō', u'\\bar{U}':u'Ū', 
      u'\\bar{Y}':u'Ȳ', u'\\bar{a}':u'ā', u'\\bar{e}':u'ē', u'\\bar{o}':u'ō', 
      u'\\bar{u}':u'ū', u'\\bar{y}':u'ȳ', u'\\breve':u'˘', u'\\breve{A}':u'Ă', 
      u'\\breve{E}':u'Ĕ', u'\\breve{G}':u'Ğ', u'\\breve{I}':u'Ĭ', 
      u'\\breve{O}':u'Ŏ', u'\\breve{U}':u'Ŭ', u'\\breve{a}':u'ă', 
      u'\\breve{e}':u'ĕ', u'\\breve{g}':u'ğ', u'\\breve{o}':u'ŏ', 
      u'\\breve{u}':u'ŭ', u'\\c':u'¸', u'\\check':u'ˇ', u'\\check{A}':u'Ǎ', 
      u'\\check{C}':u'Č', u'\\check{D}':u'Ď', u'\\check{E}':u'Ě', 
      u'\\check{G}':u'Ǧ', u'\\check{H}':u'Ȟ', u'\\check{I}':u'Ǐ', 
      u'\\check{K}':u'Ǩ', u'\\check{N}':u'Ň', u'\\check{O}':u'Ǒ', 
      u'\\check{R}':u'Ř', u'\\check{S}':u'Š', u'\\check{T}':u'Ť', 
      u'\\check{U}':u'Ǔ', u'\\check{Z}':u'Ž', u'\\check{a}':u'ǎ', 
      u'\\check{c}':u'č', u'\\check{d}':u'ď', u'\\check{e}':u'ě', 
      u'\\check{g}':u'ǧ', u'\\check{h}':u'ȟ', u'\\check{k}':u'ǩ', 
      u'\\check{n}':u'ň', u'\\check{o}':u'ǒ', u'\\check{r}':u'ř', 
      u'\\check{s}':u'š', u'\\check{u}':u'ǔ', u'\\check{z}':u'ž', 
      u'\\c{C}':u'Ç', u'\\c{D}':u'Ḑ', u'\\c{E}':u'Ȩ', u'\\c{G}':u'Ģ', 
      u'\\c{H}':u'Ḩ', u'\\c{K}':u'Ķ', u'\\c{L}':u'Ļ', u'\\c{N}':u'Ņ', 
      u'\\c{R}':u'Ŗ', u'\\c{S}':u'Ş', u'\\c{T}':u'Ţ', u'\\c{c}':u'ç', 
      u'\\c{d}':u'ḑ', u'\\c{e}':u'ȩ', u'\\c{h}':u'ḩ', u'\\c{k}':u'ķ', 
      u'\\c{l}':u'ļ', u'\\c{n}':u'ņ', u'\\c{r}':u'ŗ', u'\\c{s}':u'ş', 
      u'\\c{t}':u'ţ', u'\\dacute{O}':u'Ő', u'\\dacute{U}':u'Ű', 
      u'\\dacute{o}':u'ő', u'\\dacute{u}':u'ű', u'\\ddot':u'¨', 
      u'\\ddot{A}':u'Ä', u'\\ddot{E}':u'Ë', u'\\ddot{H}':u'Ḧ', 
      u'\\ddot{I}':u'Ï', u'\\ddot{O}':u'Ö', u'\\ddot{U}':u'Ü', 
      u'\\ddot{W}':u'Ẅ', u'\\ddot{X}':u'Ẍ', u'\\ddot{Y}':u'Ÿ', 
      u'\\ddot{a}':u'ä', u'\\ddot{e}':u'ë', u'\\ddot{h}':u'ḧ', 
      u'\\ddot{o}':u'ö', u'\\ddot{t}':u'ẗ', u'\\ddot{u}':u'ü', 
      u'\\ddot{w}':u'ẅ', u'\\ddot{x}':u'ẍ', u'\\ddot{y}':u'ÿ', 
      u'\\dgrave{A}':u'Ȁ', u'\\dgrave{E}':u'Ȅ', u'\\dgrave{I}':u'Ȉ', 
      u'\\dgrave{O}':u'Ȍ', u'\\dgrave{R}':u'Ȑ', u'\\dgrave{U}':u'Ȕ', 
      u'\\dgrave{a}':u'ȁ', u'\\dgrave{e}':u'ȅ', u'\\dgrave{o}':u'ȍ', 
      u'\\dgrave{r}':u'ȑ', u'\\dgrave{u}':u'ȕ', u'\\dot':u'˙', 
      u'\\dot{A}':u'Ȧ', u'\\dot{B}':u'Ḃ', u'\\dot{C}':u'Ċ', u'\\dot{D}':u'Ḋ', 
      u'\\dot{E}':u'Ė', u'\\dot{F}':u'Ḟ', u'\\dot{G}':u'Ġ', u'\\dot{H}':u'Ḣ', 
      u'\\dot{I}':u'İ', u'\\dot{M}':u'Ṁ', u'\\dot{N}':u'Ṅ', u'\\dot{O}':u'Ȯ', 
      u'\\dot{P}':u'Ṗ', u'\\dot{R}':u'Ṙ', u'\\dot{S}':u'Ṡ', u'\\dot{T}':u'Ṫ', 
      u'\\dot{W}':u'Ẇ', u'\\dot{X}':u'Ẋ', u'\\dot{Y}':u'Ẏ', u'\\dot{Z}':u'Ż', 
      u'\\dot{a}':u'ȧ', u'\\dot{b}':u'ḃ', u'\\dot{c}':u'ċ', u'\\dot{d}':u'ḋ', 
      u'\\dot{e}':u'ė', u'\\dot{f}':u'ḟ', u'\\dot{g}':u'ġ', u'\\dot{h}':u'ḣ', 
      u'\\dot{m}':u'ṁ', u'\\dot{n}':u'ṅ', u'\\dot{o}':u'ȯ', u'\\dot{p}':u'ṗ', 
      u'\\dot{r}':u'ṙ', u'\\dot{s}':u'ṡ', u'\\dot{t}':u'ṫ', u'\\dot{w}':u'ẇ', 
      u'\\dot{x}':u'ẋ', u'\\dot{y}':u'ẏ', u'\\dot{z}':u'ż', u'\\grave':u'`', 
      u'\\grave{A}':u'À', u'\\grave{E}':u'È', u'\\grave{I}':u'Ì', 
      u'\\grave{N}':u'Ǹ', u'\\grave{O}':u'Ò', u'\\grave{U}':u'Ù', 
      u'\\grave{W}':u'Ẁ', u'\\grave{Y}':u'Ỳ', u'\\grave{a}':u'à', 
      u'\\grave{e}':u'è', u'\\grave{n}':u'ǹ', u'\\grave{o}':u'ò', 
      u'\\grave{u}':u'ù', u'\\grave{w}':u'ẁ', u'\\grave{y}':u'ỳ', 
      u'\\hat':u'^', u'\\hat{A}':u'Â', u'\\hat{C}':u'Ĉ', u'\\hat{E}':u'Ê', 
      u'\\hat{G}':u'Ĝ', u'\\hat{H}':u'Ĥ', u'\\hat{I}':u'Î', u'\\hat{J}':u'Ĵ', 
      u'\\hat{O}':u'Ô', u'\\hat{S}':u'Ŝ', u'\\hat{U}':u'Û', u'\\hat{W}':u'Ŵ', 
      u'\\hat{Y}':u'Ŷ', u'\\hat{Z}':u'Ẑ', u'\\hat{a}':u'â', u'\\hat{c}':u'ĉ', 
      u'\\hat{e}':u'ê', u'\\hat{g}':u'ĝ', u'\\hat{h}':u'ĥ', u'\\hat{o}':u'ô', 
      u'\\hat{s}':u'ŝ', u'\\hat{u}':u'û', u'\\hat{w}':u'ŵ', u'\\hat{y}':u'ŷ', 
      u'\\hat{z}':u'ẑ', u'\\mathring':u'°', u'\\ogonek{A}':u'Ą', 
      u'\\ogonek{E}':u'Ę', u'\\ogonek{I}':u'Į', u'\\ogonek{O}':u'Ǫ', 
      u'\\ogonek{U}':u'Ų', u'\\ogonek{a}':u'ą', u'\\ogonek{e}':u'ę', 
      u'\\ogonek{i}':u'į', u'\\ogonek{o}':u'ǫ', u'\\ogonek{u}':u'ų', 
      u'\\overleftarrow':u'⟵', u'\\overrightarrow':u'⟶', u'\\rcap{A}':u'Ȃ', 
      u'\\rcap{E}':u'Ȇ', u'\\rcap{I}':u'Ȋ', u'\\rcap{O}':u'Ȏ', 
      u'\\rcap{R}':u'Ȓ', u'\\rcap{U}':u'Ȗ', u'\\rcap{a}':u'ȃ', 
      u'\\rcap{e}':u'ȇ', u'\\rcap{o}':u'ȏ', u'\\rcap{r}':u'ȓ', 
      u'\\rcap{u}':u'ȗ', u'\\slashed{O}':u'Ø', u'\\slashed{o}':u'ø', 
      u'\\subdot{A}':u'Ạ', u'\\subdot{B}':u'Ḅ', u'\\subdot{D}':u'Ḍ', 
      u'\\subdot{E}':u'Ẹ', u'\\subdot{H}':u'Ḥ', u'\\subdot{I}':u'Ị', 
      u'\\subdot{K}':u'Ḳ', u'\\subdot{L}':u'Ḷ', u'\\subdot{M}':u'Ṃ', 
      u'\\subdot{N}':u'Ṇ', u'\\subdot{O}':u'Ọ', u'\\subdot{R}':u'Ṛ', 
      u'\\subdot{S}':u'Ṣ', u'\\subdot{T}':u'Ṭ', u'\\subdot{U}':u'Ụ', 
      u'\\subdot{V}':u'Ṿ', u'\\subdot{W}':u'Ẉ', u'\\subdot{Y}':u'Ỵ', 
      u'\\subdot{Z}':u'Ẓ', u'\\subdot{a}':u'ạ', u'\\subdot{b}':u'ḅ', 
      u'\\subdot{d}':u'ḍ', u'\\subdot{e}':u'ẹ', u'\\subdot{h}':u'ḥ', 
      u'\\subdot{i}':u'ị', u'\\subdot{k}':u'ḳ', u'\\subdot{l}':u'ḷ', 
      u'\\subdot{m}':u'ṃ', u'\\subdot{n}':u'ṇ', u'\\subdot{o}':u'ọ', 
      u'\\subdot{r}':u'ṛ', u'\\subdot{s}':u'ṣ', u'\\subdot{t}':u'ṭ', 
      u'\\subdot{u}':u'ụ', u'\\subdot{v}':u'ṿ', u'\\subdot{w}':u'ẉ', 
      u'\\subdot{y}':u'ỵ', u'\\subdot{z}':u'ẓ', u'\\subhat{D}':u'Ḓ', 
      u'\\subhat{E}':u'Ḙ', u'\\subhat{L}':u'Ḽ', u'\\subhat{N}':u'Ṋ', 
      u'\\subhat{T}':u'Ṱ', u'\\subhat{U}':u'Ṷ', u'\\subhat{d}':u'ḓ', 
      u'\\subhat{e}':u'ḙ', u'\\subhat{l}':u'ḽ', u'\\subhat{n}':u'ṋ', 
      u'\\subhat{t}':u'ṱ', u'\\subhat{u}':u'ṷ', u'\\subring{A}':u'Ḁ', 
      u'\\subring{a}':u'ḁ', u'\\subtilde{E}':u'Ḛ', u'\\subtilde{I}':u'Ḭ', 
      u'\\subtilde{U}':u'Ṵ', u'\\subtilde{e}':u'ḛ', u'\\subtilde{i}':u'ḭ', 
      u'\\subtilde{u}':u'ṵ', u'\\tilde':u'˜', u'\\tilde{A}':u'Ã', 
      u'\\tilde{E}':u'Ẽ', u'\\tilde{I}':u'Ĩ', u'\\tilde{N}':u'Ñ', 
      u'\\tilde{O}':u'Õ', u'\\tilde{U}':u'Ũ', u'\\tilde{V}':u'Ṽ', 
      u'\\tilde{Y}':u'Ỹ', u'\\tilde{a}':u'ã', u'\\tilde{e}':u'ẽ', 
      u'\\tilde{n}':u'ñ', u'\\tilde{o}':u'õ', u'\\tilde{u}':u'ũ', 
      u'\\tilde{v}':u'ṽ', u'\\tilde{y}':u'ỹ', u'\\vec':u'→', 
      }

  definingfunctions = {
      u'\\newcommand':[u'[$n][$1][$2][$3][$4][$5][$6][$7][$8][$9]{$d}',u'',], 
      u'\\renewcommand':[u'[$n][$1][$2][$3][$4][$5][$6][$7][$8][$9]{$d}',u'',], 
      }

  endings = {
      u'bracket':u'}', u'complex':u'\\]', u'endafter':u'}', 
      u'endbefore':u'\\end{', u'squarebracket':u']', 
      }

  environments = {
      u'align':[u'r',u'l',], u'eqnarray':[u'r',u'c',u'l',], 
      u'gathered':[u'l',u'l',], 
      }

  fontfunctions = {
      u'\\boldsymbol':u'b', u'\\mathbb':u'span class="blackboard"', 
      u'\\mathbb{A}':u'𝔸', u'\\mathbb{B}':u'𝔹', u'\\mathbb{C}':u'ℂ', 
      u'\\mathbb{D}':u'𝔻', u'\\mathbb{E}':u'𝔼', u'\\mathbb{F}':u'𝔽', 
      u'\\mathbb{G}':u'𝔾', u'\\mathbb{H}':u'ℍ', u'\\mathbb{J}':u'𝕁', 
      u'\\mathbb{K}':u'𝕂', u'\\mathbb{L}':u'𝕃', u'\\mathbb{N}':u'ℕ', 
      u'\\mathbb{O}':u'𝕆', u'\\mathbb{P}':u'ℙ', u'\\mathbb{Q}':u'ℚ', 
      u'\\mathbb{R}':u'ℝ', u'\\mathbb{S}':u'𝕊', u'\\mathbb{T}':u'𝕋', 
      u'\\mathbb{W}':u'𝕎', u'\\mathbb{Z}':u'ℤ', u'\\mathbf':u'b', 
      u'\\mathcal':u'span class="script"', 
      u'\\mathfrak':u'span class="fraktur"', u'\\mathfrak{C}':u'ℭ', 
      u'\\mathfrak{F}':u'𝔉', u'\\mathfrak{H}':u'ℌ', u'\\mathfrak{I}':u'ℑ', 
      u'\\mathfrak{R}':u'ℜ', u'\\mathfrak{Z}':u'ℨ', u'\\mathit':u'i', 
      u'\\mathring{A}':u'Å', u'\\mathring{U}':u'Ů', u'\\mathring{a}':u'å', 
      u'\\mathring{u}':u'ů', u'\\mathring{w}':u'ẘ', u'\\mathring{y}':u'ẙ', 
      u'\\mathrm':u'span class="mathrm"', u'\\mathscr':u'span class="script"', 
      u'\\mathscr{B}':u'ℬ', u'\\mathscr{E}':u'ℰ', u'\\mathscr{F}':u'ℱ', 
      u'\\mathscr{H}':u'ℋ', u'\\mathscr{I}':u'ℐ', u'\\mathscr{L}':u'ℒ', 
      u'\\mathscr{M}':u'ℳ', u'\\mathscr{R}':u'ℛ', 
      u'\\mathsf':u'span class="mathsf"', u'\\mathtt':u'tt', 
      }

  hybridfunctions = {
      
      u'\\binom':[u'{$1}{$2}',u'f3{(}f0{f1{$1}f2{$2}}f3{)}',u'span class="binom"',u'span class="upbinom"',u'span class="downbinom"',u'span class="bigsymbol"',], 
      u'\\cfrac':[u'[$p]{$1}{$2}',u'f0{f1{$1}f2{$2}}',u'span class="fullfraction"',u'span class="numerator$p"',u'span class="denominator"',], 
      u'\\dbinom':[u'{$1}{$2}',u'f3{(}f0{f1{$1}f2{$2}}f3{)}',u'span class="fullbinom"',u'span class="upbinom"',u'span class="downbinom"',u'span class="bigsymbol"',], 
      u'\\dfrac':[u'{$1}{$2}',u'f0{f1{$1}f2{$2}}',u'span class="fullfraction"',u'span class="numerator"',u'span class="denominator"',], 
      u'\\frac':[u'{$1}{$2}',u'f0{f1{$1}f2{$2}}',u'span class="fraction"',u'span class="numerator"',u'span class="denominator"',], 
      u'\\hspace':[u'{$p}',u'f0{ }',u'span class="hspace" style="width: $p;"',], 
      u'\\leftroot':[u'{$p}',u'f0{ }',u'span class="leftroot" style="width: $p;px"',], 
      u'\\nicefrac':[u'{$1}{$2}',u'f0{f1{$1}⁄f2{$2}}',u'span class="fraction"',u'sup class="numerator"',u'sub class="denominator"',], 
      u'\\raisebox':[u'{$p}{$1}',u'f0{$1}',u'span class="raisebox" style="vertical-align: $p;"',], 
      u'\\sqrt':[u'[$0]{$1}',u'f1{$0}f0{f2{√}f3{$1}}',u'span class="sqrt"',u'sup',u'span class="radical"',u'span class="root"',], 
      u'\\tbinom':[u'{$1}{$2}',u'f3{(}f0{f1{$1}f2{$2}}f3{)}',u'span class="fullbinom"',u'span class="upbinom"',u'span class="downbinom"',u'span class="bigsymbol"',], 
      u'\\unit':[u'[$0]{$1}',u'$0f0{$1.font}',u'span class="unit"',], 
      u'\\unitfrac':[u'[$0]{$1}{$2}',u'$0f0{f1{$1.font}⁄f2{$2.font}}',u'span class="fraction"',u'sup class="unit"',u'sub class="unit"',], 
      u'\\uproot':[u'{$p}',u'f0{ }',u'span class="uproot" style="width: $p;px"',], 
      u'\\vspace':[u'{$p}',u'f0{ }',u'span class="vspace" style="height: $p;"',], 
      }

  labelfunctions = {
      u'\\label':u'a name="#"', 
      }

  limits = {
      u'commands':[u'\\sum',u'\\int',u'\\intop',], u'operands':[u'^',u'_',], 
      }

  modified = {
      u'\n':u'', u' ':u'', u'&':u'	', u'\'':u'’', u'+':u' + ', u',':u', ', 
      u'-':u' − ', u'/':u' ⁄ ', u'<':u' &lt; ', u'=':u' = ', u'>':u' &gt; ', 
      u'@':u'', u'~':u'', 
      }

  onefunctions = {
      u'\\Big':u'span class="bigsymbol"', u'\\Bigg':u'span class="hugesymbol"', 
      u'\\bar':u'span class="bar"', u'\\begin{array}':u'span class="arraydef"', 
      u'\\big':u'span class="symbol"', u'\\bigg':u'span class="largesymbol"', 
      u'\\bigl':u'span class="bigsymbol"', u'\\bigr':u'span class="bigsymbol"', 
      u'\\ensuremath':u'span class="ensuremath"', 
      u'\\hphantom':u'span class="phantom"', u'\\left':u'span class="symbol"', 
      u'\\left.':u'<span class="leftdot"></span>', 
      u'\\middle':u'span class="symbol"', 
      u'\\overbrace':u'span class="overbrace"', 
      u'\\overline':u'span class="overline"', 
      u'\\phantom':u'span class="phantom"', u'\\right':u'span class="symbol"', 
      u'\\right.':u'<span class="rightdot"></span>', 
      u'\\underbrace':u'span class="underbrace"', u'\\underline':u'u', 
      u'\\vphantom':u'span class="phantom"', 
      }

  starts = {
      u'beginafter':u'}', u'beginbefore':u'\\begin{', u'bracket':u'{', 
      u'command':u'\\', u'complex':u'\\[', u'simple':u'$', 
      u'squarebracket':u'[', u'unnumbered':u'*', 
      }

  symbolfunctions = {
      u'^':u'sup', u'_':u'sub', 
      }

  textfunctions = {
      u'\\mbox':u'span class="mbox"', u'\\text':u'span class="text"', 
      u'\\textbf':u'b', u'\\textipa':u'span class="textipa"', u'\\textit':u'i', 
      u'\\textrm':u'span class="mathrm"', 
      u'\\textsc':u'span class="versalitas"', 
      u'\\textsf':u'span class="mathsf"', u'\\textsl':u'i', u'\\texttt':u'tt', 
      u'\\textup':u'span class="normal"', 
      }

  underdecoratingfunctions = {
      u'\\r':u'∘', u'\\s':u'ˌ', u'\\textsubring':u'∘', 
      }

  unmodified = {
      
      u'characters':[u'.',u'*',u'€',u'(',u')',u'[',u']',u':',u'·',u'!',u';',u'|',u'§',u'"',], 
      }

class GeneralConfig(object):
  "Configuration class from config file"

  version = {
      u'date':u'2010-05-10', u'lyxformat':u'345', u'number':u'0.44', 
      }

class HeaderConfig(object):
  "Configuration class from config file"

  parameters = {
      u'beginpreamble':u'\\begin_preamble', u'branch':u'\\branch', 
      u'documentclass':u'\\textclass', u'endbranch':u'\\end_branch', 
      u'endpreamble':u'\\end_preamble', u'language':u'\\language', 
      u'lstset':u'\\lstset', u'paragraphseparation':u'\\paragraph_separation', 
      u'pdftitle':u'\\pdf_title', u'secnumdepth':u'\\secnumdepth', 
      u'tocdepth':u'\\tocdepth', 
      }

  styles = {
      
      u'article':[u'article',u'aastex',u'aapaper',u'acmsiggraph',u'sigplanconf',u'achemso',u'amsart',u'apa',u'arab-article',u'armenian-article',u'article-beamer',u'chess',u'dtk',u'elsarticle',u'heb-article',u'IEEEtran',u'iopart',u'kluwer',u'scrarticle-beamer',u'scrartcl',u'extarticle',u'paper',u'mwart',u'revtex4',u'spie',u'svglobal3',u'ltugboat',u'agu-dtd',u'jgrga',u'agums',u'entcs',u'egs',u'ijmpc',u'ijmpd',u'singlecol-new',u'doublecol-new',u'isprs',u'tarticle',u'jsarticle',u'jarticle',u'jss',u'literate-article',u'siamltex',u'cl2emult',u'llncs',u'svglobal',u'svjog',u'svprobth',], 
      }

class ImageConfig(object):
  "Configuration class from config file"

  converters = {
      
      u'imagemagick':u'convert [-density $scale] [-pepito $juanito] [-tonto $decapi] -define pdf:use-cropbox=true "$input" "$output"', 
      u'inkscape':u'inkscape "$input" --export-png="$output"', 
      }

  formats = {
      u'default':u'.png', u'raster':[u'.png',u'.jpg',], 
      u'vector':[u'.svg',u'.eps',], 
      }

  size = {
      u'ignoredtexts':[u'col',u'text',u'line',u'page',u'theight',u'pheight',], 
      }

class NewfangleConfig(object):
  "Configuration class from config file"

  constants = {
      u'chunkref':u'chunkref{', u'endcommand':u'}', u'endmark':u'&gt;', 
      u'startcommand':u'\\', u'startmark':u'=&lt;', 
      }

class NumberingConfig(object):
  "Configuration class from config file"

  layouts = {
      
      u'ordered':[u'Chapter',u'Section',u'Subsection',u'Subsubsection',u'Paragraph',], 
      u'unique':[u'Part',u'Book',], 
      }

class StyleConfig(object):
  "Configuration class from config file"

  quotes = {
      u'ald':u'»', u'als':u'›', u'ard':u'«', u'ars':u'‹', u'eld':u'“', 
      u'els':u'‘', u'erd':u'”', u'ers':u'’', u'fld':u'«', u'fls':u'‹', 
      u'frd':u'»', u'frs':u'›', u'gld':u'„', u'gls':u'‚', u'grd':u'“', 
      u'grs':u'‘', u'pld':u'„', u'pls':u'‚', u'prd':u'”', u'prs':u'’', 
      u'sld':u'”', u'srd':u'”', 
      }

  spaces = {
      u'\\enskip{}':u' ', u'\\hfill{}':u'<span class="hfill"> </span>', 
      u'\\hspace*{\\fill}':u' ', u'\\hspace*{}':u'', u'\\hspace{}':u' ', 
      u'\\negthinspace{}':u'', u'\\qquad{}':u'  ', u'\\quad{}':u' ', 
      u'\\space{}':u' ', u'\\thinspace{}':u' ', u'~':u' ', 
      }

class TagConfig(object):
  "Configuration class from config file"

  barred = {
      u'under':u'u', 
      }

  family = {
      u'sans':u'span class="sans"', u'typewriter':u'tt', 
      }

  flex = {
      u'CharStyle:Code':u'span class="code"', 
      u'CharStyle:MenuItem':u'span class="menuitem"', 
      }

  layouts = {
      u'Center':u'div', u'Chapter':u'h?', u'Date':u'h2', u'Paragraph':u'div', 
      u'Part':u'h1', u'Quotation':u'blockquote', u'Quote':u'blockquote', 
      u'Section':u'h?', u'Subsection':u'h?', u'Subsubsection':u'h?', 
      }

  listitems = {
      u'Enumerate':u'ol', u'Itemize':u'ul', 
      }

  notes = {
      u'Comment':u'', u'Greyedout':u'span class="greyedout"', u'Note':u'', 
      }

  shaped = {
      u'italic':u'i', u'slanted':u'i', u'smallcaps':u'span class="versalitas"', 
      }

class TranslationConfig(object):
  "Configuration class from config file"

  constants = {
      u'Book':u'Book', u'Chapter':u'Chapter', u'Paragraph':u'Paragraph', 
      u'Part':u'Part', u'Section':u'Section', u'Subsection':u'Subsection', 
      u'Subsubsection':u'Subsubsection', u'abstract':u'Abstract', 
      u'bibliography':u'Bibliography', u'figure':u'figure', 
      u'float-algorithm':u'Algorithm ', u'float-figure':u'Figure ', 
      u'float-listing':u'Listing ', u'float-table':u'Table ', 
      u'float-tableau':u'Tableau ', u'index':u'Index', 
      u'jsmath-enable':u'Please enable JavaScript on your browser.', 
      u'jsmath-requires':u' requires JavaScript to correctly process the mathematics on this page. ', 
      u'jsmath-warning':u'Warning: ', u'list-algorithm':u'List of Algorithms', 
      u'list-figure':u'List of Figures', u'list-table':u'List of Tables', 
      u'list-tableau':u'List of Tableaux', u'next':u'Next', 
      u'nomenclature':u'Nomenclature', u'on-page':u' on page ', 
      u'prev':u'Previous', u'toc':u'Table of Contents', u'up':u'Up', 
      }

  languages = {
      u'deutsch':u'de', u'dutch':u'nl', u'english':u'en', u'french':u'fr', 
      u'ngerman':u'de', u'spanish':u'es', 
      }

