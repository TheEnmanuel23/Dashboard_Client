import sqlparse
from sqlparse.tokens import Keyword

class ConfigSQL:
	def settingSql(self, sqlOriginal, callback_sqlWithNewWhere):
		sqlParsed = self.getSqlParsed(sqlOriginal)
		sqlAfterClauseFrom = self.extractSqlAfterClauseFrom(sqlParsed)
		queryFormated =  sqlOriginal.replace(sqlAfterClauseFrom, '')
		sqlWithNewWhere = callback_sqlWithNewWhere(queryFormated, sqlParsed)
		newQuery = "%s %s" % (sqlWithNewWhere, sqlAfterClauseFrom)
		return newQuery

	def getSqlParsed(self, sql):
		return sqlparse.parse(sql)[0]

	def extractSqlAfterClauseFrom(self, sqlParsed):
		sqlAfterClauseFrom = ''
		keyword_FROM_finded = False
		clause_FROM_finalized = False
		for token in sqlParsed:
			if keyword_FROM_finded:				
				if clause_FROM_finalized:					
					sqlAfterClauseFrom += token.value
				elif token.ttype is Keyword:
					sqlAfterClauseFrom += token.value
					clause_FROM_finalized = True
			elif token.ttype is Keyword and token.value.upper() == 'FROM':
				keyword_FROM_finded = True
		return sqlAfterClauseFrom